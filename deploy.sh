#!/bin/sh

while getopts 'k:s:' OPTION ; do
	case "${OPTION}" in
	k)
		AWS_KEY=$OPTARG
		;;
	s)
		AWS_SECRET=$OPTARG
		;;
	esac
done

function usage {
	echo "Usage:"
	echo " $0 -k <AWS_ACCESS_KEY_ID> -s <AWS_SECRET_ACCESS_KEY> "
	exit $1
}

function setAwsCredentials {
	export AWS_ACCESS_KEY_ID=$AWS_KEY
	export AWS_SECRET_ACCESS_KEY=$AWS_SECRET
}

function checkRequiredArguments {
	if [ -z "${AWS_KEY}" ]; then
		echo "$0: missing required option -- k"
		echo
		usage 1
	fi

	if [ -z "${AWS_SECRET}" ]; then
		echo "$0: missing required option -- s"
		echo
		usage 1
	fi

	setAwsCredentials
}

function deploymentSteps {
	#create DB backup and download it
	echo "Creating DB backup and download it"
	heroku pgbackups:capture
	curl -o latest.dump `heroku pgbackups:url`

	#push to heroku
	echo "Push changes to heroku ..."
	git push heroku master

	#sync files with S3
	echo "Sync files with s3 ..."
	aws s3 sync sites/icon/static s3://icon-oscar/ --acl public-read --region=eu-west-1
	aws s3 sync /Users/pavelbogomolenko/Documents/www/misc/py/django/oscarenv2.7/lib/python2.7/site-packages/Django-1.6.1-py2.7.egg/django/contrib/admin/static/admin s3://icon-oscar/admin --acl public-read --region=eu-west-1

	#clean-up S3 files
	echo "Clean up s3 folder from backup files ..."
	aws s3 rm s3://icon-oscar/ --recursive  --exclude "*" --include "*_1.js" --include "*_1.jpg" --include "*_1.gif" --include "*_1.css" --include "*_1.eot" --include "*_1.ttf" --include "*_1.svg" --include "*_1.woff" --region=eu-west-1
}

function main {
	checkRequiredArguments
	deploymentSteps
}

#run
main
