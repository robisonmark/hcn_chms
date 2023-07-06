from .base import *
import configparser

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

parser = configparser.ConfigParser()
parser.read("../db.conf")

sections = parser.sections()

SECRET_KEY = parser['django']['secrets']
USER = parser.get("DB", "user")
NAME = "hcn_chms"
PASSWORD = parser.get("DB", "password")
HOST = parser.get("DB", "host")
PORT = parser.get("DB", 'port')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': PORT,
    }
}

# ALLOWED_HOSTS = ['localhost:3000','*.robros.dev', '138.197.100.63']
ALLOWED_HOSTS = ['*']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/matt/hcn_chms/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

CORS_ALLOWED_ORIGINS = [
   '*'
]

CSRF_TRUSTED_ORIGINS = [
   '*'
]
