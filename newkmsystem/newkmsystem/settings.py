"""
Django settings for newkmsystem project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y5jg8^7a9!nr(io1@th9ib4m*olua+u-wyes7j1j8fk-!$+j*f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	
	'home',

	'registration',
	#use table as same with form
	'django_tables2',
	#navigation for tag
	'navigation',
	#set pages
	'pagination',
	'datetimewidget',
	
	'manpower',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	#for page app
	'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'newkmsystem.urls'

WSGI_APPLICATION = 'newkmsystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
#For django tables2 app
TEMPLATE_CONTEXT_PROCESSORS+=(
	'django.core.context_processors.request',
)
#For django pagination app
TEMPLATE_CONTEXT_PROCESSORS+=(
	"django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

TEMPLATE_DIRS=('./templates',)
#registration set due to use "django-registration-redux"
REGISTRATION_OPEN=True
ACCOUNT_ACTIVATION_DAYS=7
REGISTRATION_AUTO_LOGIN=True
LOGIN_REDIRECT_URL='/accounts/'
LOGIN_URL='/accounts/login/'