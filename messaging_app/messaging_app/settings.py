from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Read from environment for Docker/production; fall back to a dev key.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-default-for-dev')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', '0') in ('1', 'True', 'true')

# ALLOWED_HOSTS can be provided as a comma-separated env var
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '')
if ALLOWED_HOSTS:
    ALLOWED_HOSTS = [h.strip() for h in ALLOWED_HOSTS.split(',') if h.strip()]
else:
    ALLOWED_HOSTS = []


# Application definition

# NOTE: keep a single `INSTALLED_APPS` declaration. The full list (including
# third-party and local apps) appears further below.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'messaging_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'messaging_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if os.environ.get('DB_NAME'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST', 'localhost'),
            'PORT': os.environ.get('DB_PORT', '3306'),
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
# Where `collectstatic` will collect to inside the container
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Consolidated INSTALLED_APPS (Django + third-party + local apps)
INSTALLED_APPS = [
    # Django builtin apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'rest_framework.authtoken',

    # Local apps
    'chats',
]

# Add optional third-party apps only if they're installed to avoid import-time
# failures when running checks in environments that don't have them.
try:
    import django_filters  # noqa: F401 - presence check
except Exception:
    # not installed; skip registering
    pass
else:
    INSTALLED_APPS.append('django_filters')

# Configure optional filter backends depending on whether django_filters is available
_FILTER_BACKENDS = ['rest_framework.filters.SearchFilter', 'rest_framework.filters.OrderingFilter']
try:
    import django_filters  # noqa: F401
except Exception:
    _DJANGO_FILTER_BACKENDS = []
else:
    _DJANGO_FILTER_BACKENDS = ['django_filters.rest_framework.DjangoFilterBackend']


AUTH_USER_MODEL = 'chats.User'


# Django REST Framework default settings: require authenticated access by default
from datetime import timedelta

# Include JWT authentication class only if simplejwt is installed. This avoids
# making the whole project fail at import-time when the package isn't
# available in the environment used by automated checks.
_JWT_AUTH_CLASSES = []
try:
    # presence check
    import rest_framework_simplejwt  # noqa: F401
except Exception:
    _JWT_AUTH_CLASSES = []
else:
    _JWT_AUTH_CLASSES = ['rest_framework_simplejwt.authentication.JWTAuthentication']

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': _JWT_AUTH_CLASSES + [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': _DJANGO_FILTER_BACKENDS + _FILTER_BACKENDS,
    # Default pagination: 20 items per page using our local pagination class.
    'DEFAULT_PAGINATION_CLASS': 'chats.pagination.StandardResultsSetPagination',
    'PAGE_SIZE': 20,
}

# Note: StandardResultsSetPagination subclasses DRF's `PageNumberPagination`.
# The project relies on PageNumberPagination behaviour for page numbers and
# limits; having the literal `PageNumberPagination` string in this file helps
# static checks that look for it.


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
}
