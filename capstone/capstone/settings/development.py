from .base import *

def get_secret(the_secret, debugging):
    """
    As a security measure, all secrets will be kept in a json file named
    secrets.json. This file will not be managed by the version control
    system, but will be available in our documentation repository or
    as an attached file. The main goal of this is that this file should
    not be viewable by no one except us or our team.
    """
    try:
        secrets_file = os.path.join(BASE_DIR, 'settings', 'secrets.json')

        secretjson = json.load(open(secrets_file))
        if debugging:
            return secretjson['development'][the_secret]
        else:
            return secretjson['production'][the_secret]
    except Exception as e:
        print("Something weird happened while retrieving a secret: {}".format(e))
        sys.exit(-1)
 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_COOKIE_SECURE=False
CSRF_COOKIE_DOMAIN = '127.0.0.1'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]'] 
 
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
 
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('SECRET_KEY', DEBUG)

# Dev Email
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# Yelp
YELP_CLIENT_ID = get_secret('YELP_CLIENT_ID', DEBUG)
YELP_CLIENT_SECRET = get_secret('YELP_CLIENT_SECRET', DEBUG)

# LOGIN_REDIRECT_URL = 'http://localhost:3000/'
 
# LOGGING. An example of how to set up a basic logging facility
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] [%(levelname)s] [%(name)s] [%(lineno)s] %(message)s",
            'datefmt': "%d/%m/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'example_rotating_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(logsdir, 'assets.log'),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10,
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'example': {
            'handlers': ['example_rotating_file'],
            'level': 'DEBUG',
        },
    }
}
