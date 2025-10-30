from .base import *
import os
import dj_database_url

# --------------------------
# SECURITY SETTINGS
# --------------------------
DEBUG = False
SECRET_KEY = os.getenv("SECRET_KEY", "replace-this-with-a-secure-key")

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "[::1]",
    "food-api-website.onrender.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://food-api-website.onrender.com",
]

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# --------------------------
# EMAIL CONFIGURATION
# --------------------------
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASS")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER or "webmaster@food-api-website.onrender.com"

# --------------------------
# THIRD-PARTY KEYS
# --------------------------
YELP_CLIENT_ID = os.getenv("YELP_CLIENT_ID", "")
YELP_CLIENT_SECRET = os.getenv("YELP_CLIENT_SECRET", "")

# --------------------------
# DATABASE CONFIGURATION
# --------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    )
}

# --------------------------
# STATIC FILES
# --------------------------
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# --------------------------
# LOGGING
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
    },
    "root": {"handlers": ["console"], "level": "INFO"},
}
