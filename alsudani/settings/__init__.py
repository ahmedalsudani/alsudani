__author__ = 'ahmed'

# Prevent submodules from being recognized as settings
__all__ = []

from os import environ
from .base import *

try:
    environment_type = environ['ENVIRONMENT']
except:
    environment_type = 'dev'

if (environment_type == 'PRODUCTION'):
    from .production import *
else:
    from .dev import *
