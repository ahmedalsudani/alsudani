__author__ = 'ahmed'

import os
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ['APP_SECRET_KEY']
DEBUG = False

# Database

DATABASES = {
    'default': dj_database_url.config(default=os.environ['DATABASE_URL'])

    # RDS on ELB
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': os.environ['RDS_DB_NAME'],
    #     'USER': os.environ['RDS_USERNAME'],
    #     'PASSWORD': os.environ['RDS_PASSWORD'],
    #     'HOST': os.environ['RDS_HOSTNAME'],
    #     'PORT': os.environ['RDS_PORT'],
    # }
}

# Google analytics
GA_CODE = os.environ['GA_CODE']

# Statcounter
SC_PROJECT, SC_SECURITY = os.environ['SC_CREDS'].split(r':')

STATIC_URL = os.environ['CDN_ADDRESS']

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']

AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
