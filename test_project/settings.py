"""
Django settings for test_project project.

Generated by 'django-admin startproject' using Django 1.8.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '37r=l^!c^1-7o8z2luc%a1x&)jt^9v+ockis0ql7k_y*lm555('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'paperclip',
    'djgeojson',
    'compressor',
    'easy_thumbnails',
    'crispy_forms',
    'rest_framework',
    'embed_video',
    'mapentity',  # Make sure mapentity settings are loaded before leaflet ones
    'leaflet',
    'test_app',
    'modeltranslation'
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'mapentity.middleware.AutoLoginMiddleware',
)

ROOT_URLCONF = 'test_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'djappypod.backend.OdtTemplates',
    },
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
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'mapentity.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'test_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR, 'database.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGES = (
    ('en', "English"),
    ('fr', "French"),
)
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

MEDIA_URL = '/media/'
MEDIA_URL_SECURE = '/media_secure/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SRID = 2154
COMPRESS_ENABLED = False
TEST = True

MAPENTITY_CONFIG = {
    'SENDFILE_HTTP_HEADER': 'X-Accel-Redirect',
}

PAPERCLIP_FILETYPE_MODEL = 'test_app.FileType'
PAPERCLIP_ATTACHMENT_MODEL = 'test_app.Attachment'

if os.path.exists('/usr/lib/x86_64-linux-gnu/mod_spatialite.so'):
    SPATIALITE_LIBRARY_PATH = '/usr/lib/x86_64-linux-gnu/mod_spatialite'

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(name)s %(pathname)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
    },
}

LEAFLET_CONFIG = {
    'SRID': 3857,
    'TILES': [
        ('OSM', 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', '(c) OpenStreetMap Contributors'),
        ('OSM N&B', 'http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png', '(c) OpenStreetMap Contributors'),
    ],
    'SPATIAL_EXTENT': (1.3, 43.7, 1.5, 43.5),
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

MAPENTITY_CONFIG = {
    'CONVERSION_SERVER': 'http://localhost/',
    'CAPTURE_SERVER': 'http://localhost/',
    'SENDFILE_HTTP_HEADER': 'X-Accel-Redirect',
}

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
