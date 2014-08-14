"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4#f=%^g3p!8)lx5-=c*$sd9#3e(x3nea0@p2em7a@(t-vagx82'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crm',
    'devices',
    'config',
    'south',
#    'guardian',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-en'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = False

USE_TZ = True

TIME_FORMAT = 'H:i'

DATETIME_FORMAT = 'D d-m-Y H:i'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#STATIC_ROOT = '/Users/konradsierzputowski/python/test/mysite'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

TEMPLATE_DIRS = (
    '/Users/konradsierzputowski/python/test/mysite/templates', # Change this to your own directory.
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)
"""
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'guardian.backends.ObjectPermissionBackend',
)

ANONYMOUS_USER_ID = 1"""

GRAPPELLI_ADMIN_TITLE = "Omni3D CRM"
GRAPPELLI_SWITCH_USER = True
GRAPPELLI_AUTOCOMPLETE_LIMIT=5

GRAPPELLI_AUTOCOMPLETE_SEARCH_FIELDS = {
    "crm": {
        "company": ("id__iexact", "name__icontains",),
        "person": ("id__iexact", "name__icontains",),
        "device": ("id__iexact", "name__icontains",),
        "order": ("id__iexact", "name__icontains",)
    }
}
#GRAPPELLI_INDEX_DASHBOARD = 'crm.dashboard.CustomIndexDashboard'
