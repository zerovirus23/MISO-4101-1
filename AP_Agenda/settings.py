"""
Django settings for AP_Agenda project.
For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cso^6u_18vb7@8+acz+b)81$09rj*10_gvp5&^kep@qrr$+6o9'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'agenda.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



ROOT_URLCONF = 'AP_Agenda.urls'
#WSGI_APPLICATION = 'wsgi.application'
WSGI_APPLICATION = 'AP_Agenda.wsgi.application'
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#DB_HOST = 'ec2-174-129-213-103.compute-1.amazonaws.com'
#DB_NAME = 'ddp1cg8vp0hgem'
#DB_USER = 'jklrkeighrrgdv'
#DB_USER_PASSWORD = 'VX6mBzpZF-v7aUIvTRprcUHhZi'



DB_HOST = 'localhost'
DB_USER = 'postgres'
DB_USER_PASSWORD = 'postgres'
DB_NAME = 'agenda'
    
#DATABASES = {
#        'default': {
#                    'ENGINE': 'django.db.backends.postgresql_psycopg2',
#                    'NAME': 'agenda',
#                    'USER': 'postgres',
#                    'PASSWORD': '000000',
#                    'HOST': 'localhost',
#                    'PORT': '5432',
#                    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_USER_PASSWORD,
        'HOST': DB_HOST,
        'PORT': '5432',
        'TEST': 
        {
        'NAME': 'agenda1',

        }
        
    }
}

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()
 
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
 
# Allow all host headers
#ALLOWED_HOSTS = ['*']
 
# Static asset configuration
#import os
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
 

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
 
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


#Custome template folder
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
LOGIN_REDIRECT_URL='/'
LOGIN_URL='/login/'
MYTIMER = 2

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


