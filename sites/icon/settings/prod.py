# -*- coding: utf-8 -*-

from common import *

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['.herokuapp.com', 'gallery-obraz.com', 'www.gallery-obraz.com']

# LESS/CSS/statics
# ================
#USE_LESS = True
#COMPRESS_ENABLED = True

STATIC_URL = 'https://icon-oscar.s3.amazonaws.com/'
COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = STATIC_ROOT

#aws configuration
if 'S3_KEY' in os.environ and 'S3_SECRET' in os.environ:
	AWS_ACCESS_KEY_ID = os.environ['S3_KEY']
	AWS_SECRET_ACCESS_KEY = os.environ['S3_SECRET']

# aws S3 bucket configuration
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'icon-oscar'
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#COMPRESS_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'sites.icon.apps.oscartweaks.storage.cacheds3boto.CachedS3BotoStorage'
COMPRESS_STORAGE = 'sites.icon.apps.oscartweaks.storage.cacheds3boto.CachedS3BotoStorage'
AWS_S3_FILE_OVERWRITE = False
AWS_PRELOAD_METADATA = True

# see http://developer.yahoo.com/performance/rules.html#expires
# AWS_HEADERS = {
# 	'Expires': 'Thu, 15 Apr 2010 20:00:00 GMT',
# 	'Cache-Control': 'max-age=86400',
# }

INSTALLED_APPS = INSTALLED_APPS + ['sites.icon.apps.oscartweaks']
