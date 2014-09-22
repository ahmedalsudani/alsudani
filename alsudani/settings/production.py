__author__ = 'ahmed'

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ['APP_SECRET_KEY']
DEBUG = False

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT'],
    }
}

# Google analytics
GA_CODE = os.environ['GA_CODE']

# Statcounter
SC_PROJECT, SC_SECURITY = os.environ['SC_CREDS'].split(r':')
