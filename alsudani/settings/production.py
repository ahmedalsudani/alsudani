__author__ = 'ahmed'

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ['APP_SECRET_KEY']
DEBUG = False

# Database
