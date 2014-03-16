# -*- coding: utf-8 -*-

from common import *

ALLOWED_HOSTS = ['127.0.0.1']

USE_TZ = True

DEBUG = True
TEMPLATE_DEBUG = True
SQL_DEBUG = True
SEND_BROKEN_LINK_EMAILS = False

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'oscar-icon',
		'USER': 'oscar-icon',
		'PASSWORD': '',
		'HOST': '127.0.0.1',
		'PORT': '',
	}
}

INSTALLED_APPS = INSTALLED_APPS + ['apps.oscartweaks']

