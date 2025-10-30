from .base import *
import os

# --------------------------
# DEBUG & HOST CONFIGURATION
# --------------------------
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = False  # relaxed for local dev
CSRF_COOKIE_SECURE = False
CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "https://127.0.0.1",
]
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

# --------------------------
# SECURITY & SECRET KEY
# --------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-dev-key")

# --------------------------
# EMAIL CONFIGURATION
# --------------------------
EMAIL_HOST = os.getenv("EMAIL_HOST", "localhost")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "1025"))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "False").lower() == "true"
EMAIL_HOST_USER = os.getenv("EMAIL_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASS", "")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER or "webmaster@localhost"

# --------------------------
# THIRD-PARTY API KEYS
# --------------------------
YELP_CLIENT_ID = os.getenv("YELP_CLIENT_ID", "")
YELP_CLIENT_SECRET = os.getenv("YELP_CLIENT_SECRET", "")

# --------------------------
# LOGGING CONFIGURATION
# --------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] [%(levelname)s] [%(name)s] [%(lineno)s] %(message)s",
            "datefmt": "%d/%m/%Y %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simple"},
        "example_rotating_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "verbose",
            "filename": os.path.join(logsdir, "assets.log"),
            "maxBytes": 1024 * 1024 * 10,
            "backupCount": 10,
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": True,
        },
        "example": {
            "handlers": ["example_rotating_file"],
            "level": "DEBUG",
        },
    },
}
from .base import *
import os

# --------------------------
# DEBUG & HOST CONFIGURATION
# --------------------------
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = False  # relaxed for local dev
CSRF_COOKIE_SECURE = False
CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "https://127.0.0.1",
]
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

# --------------------------
# SECURITY & SECRET KEY
# --------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-dev-key")

# --------------------------
# EMAIL CONFIGURATION
# --------------------------
EMAIL_HOST = os.getenv("EMAIL_HOST", "localhost")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "1025"))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "False").lower() == "true"
EMAIL_HOST_USER = os.getenv("EMAIL_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASS", "")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER or "webmaster@localhost"

# --------------------------
# THIRD-PARTY API KEYS
# --------------------------
YELP_CLIENT_ID = os.getenv("YELP_CLIENT_ID", "")
YELP_CLIENT_SECRET = os.getenv("YELP_CLIENT_SECRET", "")

# --------------------------
# LOGGING CONFIGURATION
# --------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] [%(levelname)s] [%(name)s] [%(lineno)s] %(message)s",
            "datefmt": "%d/%m/%Y %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simple"},
        "example_rotating_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "verbose",
            "filename": os.path.join(logsdir, "assets.log"),
            "maxBytes": 1024 * 1024 * 10,
            "backupCount": 10,
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": True,
        },
        "example": {
            "handlers": ["example_rotating_file"],
            "level": "DEBUG",
        },
    },
}
