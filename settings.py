import os
import sys
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

# Get the Heroku config var for SERVER_CONFIG, if it's not present, then local
# https://devcenter.heroku.com/articles/config-vars
SERVER_CONFIG = os.environ.get('SERVER_CONFIG', 'local')

PROJECT_ROOT = os.path.dirname(__file__)
DEBUG = True if SERVER_CONFIG != 'prod' else False

TEMPLATE_DEBUG = DEBUG

for path in ('vendor','utils'):
    sys.path.insert(0, os.path.join(PROJECT_ROOT, path))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Jeremiah Malina', 'jmalina327@gmail.com'),
    ('Misha Ponizil', 'misha.ponizil@gmail.com'),
)

MANAGERS = ADMINS

# Testing
TEST = False
if 'test' in sys.argv:
    TEST = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'feedbackmachine'
        }
    }
    SOUTH_TESTS_MIGRATE = False

#
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': '',                      # Or path to database file if using sqlite3.
#         'USER': '',                      # Not used with sqlite3.
#         'PASSWORD': '',                  # Not used with sqlite3.
#         'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#     }
# }
#
#
# DO NOT CHANGE THIS DATABASE SETTING
# TO RUN LOCALLY, CREATE A local_settings.py FILE AND PUT COPY THE DATABASES
# SETTING ABOVE WITH THE RIGHT CONFIG TO OVERRIDE HEROKU DB SETTINGS
if not TEST:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'US/Eastern'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static"
STATIC_URL = 'https://s3.amazonaws.com/feedbackmachine/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = 'https://s3.amazonaws.com/feedbackmachine/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    PROJECT_ROOT + '/static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATICFILES_STORAGE = 'utils.storage.CachedS3BotoStorage'


# S3 Setup
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_HEADERS = {
    'Cache-Control': 'max-age=86400',
}
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
AWS_STORAGE_BUCKET_NAME = 'feedbackmachine'
AWS_QUERYSTRING_AUTH = False    # http://code.welldev.org/django-storages/issue/51/please-improve-s3-storage-documentation
AWS_S3_SECURE_URLS = True
AWS_PRELOAD_METADATA = True
# This is needed to prevent django-storages from hitting S3 each and every time we get the url property of an image
# AWS_S3_CUSTOM_DOMAIN = ''


# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    '(pg^hlqx!j!uoh=#)e8v63+hldy)wlp=+rv92a48(ve61l)!+w'
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'utils.middleware.static_url.StaticUrlMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
# WSGI_APPLICATION = 'feedbackmachine.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'gunicorn',
    'app',
    'compressor',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


#
# Compressor settings
# http://django_compressor.readthedocs.org/en/latest/remote-storages/
#
INSTALLED_APPS += ('compressor',)
COMPRESS_ENABLED = SERVER_CONFIG == 'prod'
COMPRESS_STORAGE = STATICFILES_STORAGE
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_OUTPUT_DIR = 'compressed'
COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
)
COMPRESS_JS_FILTERS = (
    'compressor.filters.jsmin.JSMinFilter',
)


try:
    from local_settings import *
except ImportError:
    pass
