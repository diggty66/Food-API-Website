"""
Base Django settings for the capstone project.
Used by both development.py and production.py
"""

import os
import posixpath
import sys
from pathlib import Path
from dotenv import load_dotenv

# --------------------------
# PATHS
# --------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # points to project root (where manage.py lives)

# Load environment variables
load_dotenv(BASE_DIR / ".env")

# Static, media, and template directories
TEMPLATE_DIR = BASE_DIR / 'templates'
STATIC_DIR = BASE_DIR / 'static'
MEDIA_DIR = BASE_DIR / 'media'

# --------------------------
# PATHS
# --------------------------
# Current file: capstone/settings/base.py
# BASE_DIR should point to the project root (where manage.py lives)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static, media, and template directories
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],  # uses your variable from above
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --------------------------
# SECURITY & HOSTS
# --------------------------
ALLOWED_HOSTS = []  # overridden in production.py

# --------------------------
# APPLICATIONS
# --------------------------
INSTALLED_APPS = [
    'capstone.app',
    'capstone.capstone',

    # Django built-ins
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'django_jinja',
]

# --------------------------
# MIDDLEWARE
# --------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --------------------------
# URLS & WSGI
# --------------------------
ROOT_URLCONF = 'capstone.capstone.urls'
WSGI_APPLICATION = 'capstone.capstone.wsgi.application'

# --------------------------
# DATABASE
# --------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# --------------------------
# PASSWORD VALIDATION
# --------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------
# INTERNATIONALIZATION
# --------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# --------------------------
# STATIC & MEDIA
# --------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR]  # ✅ restore static dir usage for local dev
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # ✅ correct for collectstatic
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR

# --------------------------
# LOGIN
# --------------------------
LOGIN_URL = '/app/user_login/'

# --------------------------
# LOGGING
# --------------------------
logsdir = os.path.realpath(os.path.join(BASE_DIR, 'logs'))

try:
    os.makedirs(logsdir, exist_ok=True)
except OSError as e:
    print(f"OSError({e.errno}): {e.strerror}")
    sys.exit(1)
