"""
Django settings for AP_Agenda project.

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
SECRET_KEY = 'cso^6u_18vb7@8+acz+b)81$09rj*10_gvp5&^kep@qrr$+6o9'

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
    'agenda',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


)


ROOT_URLCONF = 'AP_Agenda.urls'

WSGI_APPLICATION = 'AP_Agenda.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5snf1vtia97an',
        'USER': 'rmwbyxiytiwdzq',
        'PASSWORD': 'RMxz34GI7yhQV0Cxs_ayf3dMD9',
        'HOST': 'ec2-54-83-205-46.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = 'admin/app/static/'
#os.path.join('http://desa-1.herokuapp.com',BASE_DIR, 'static/')
#STATIC_ROOT = '/static/'
STATIC_ROOT = 'tmp/'

STATICFILES_DIRS = (
    os.path.join('http://desa-1.herokuapp.com',BASE_DIR, 'static/'),
)

#Custome template folder
#TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
