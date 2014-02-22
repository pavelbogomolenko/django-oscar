# -*- coding: utf-8 -*-

from common import *

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# LESS/CSS/statics
# ================
USE_LESS = True
COMPRESS_ENABLED = True

STATIC_URL = 'https://icon-oscar.s3.amazonaws.com/'

#aws configuration
AWS_ACCESS_KEY_ID = 'AKIAJLIWRCZ2D3SSRD7A'
AWS_SECRET_ACCESS_KEY = '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'

# aws S3 bucket configuration
#DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'icon-oscar'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_FILE_OVERWRITE = False

# see http://developer.yahoo.com/performance/rules.html#expires
AWS_HEADERS = {
'Expires': 'Thu, 15 Apr 2010 20:00:00 GMT',
'Cache-Control': 'max-age=86400',
}
COMPRESS_OFFLINE = True
