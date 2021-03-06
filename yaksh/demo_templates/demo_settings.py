"""
Django settings for my_demo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import tempfile
from yaksh.pipeline.settings import AUTH_PIPELINE

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# The directory where user data can be saved.
OUTPUT_DIR = os.path.join(tempfile.gettempdir(), 'output')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'TH!S_!S_@_DUMMY_K3Y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

URL_ROOT = ''

# Application definition

FIXTURE_DIRS = ('{{ fixture_dir }}')

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'yaksh',
    'taggit',
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'yaksh.middleware.one_session_per_user.OneSessionPerUserMiddleware',
    'yaksh.middleware.user_time_zone.TimezoneMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = '{{ root_urlconf }}'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = '/exam/login/'

LOGIN_REDIRECT_URL = '/exam/'

MEDIA_URL = "/data/"

MEDIA_ROOT = os.path.join(BASE_DIR, "yaksh", "data")

SOCIAL_AUTH_LOGIN_ERROR_URL = '/exam/login/'

EMAIL_USE_TLS = False

EMAIL_HOST = 'your_email_host'

EMAIL_PORT = 'your_email_port'

EMAIL_HOST_USER = 'email_host_user'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': ['yaksh/templates'],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
            'debug': False,
        }
    },
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'GOOGLE_KEY_PROVIDED'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'GOOGLE_SECRET_PROVIDED'

SOCIAL_AUTH_FACEBOOK_KEY = 'FACEBOOK_KEY_PROVIDED'
SOCIAL_AUTH_FACEBOOK_SECRET = 'FACEBOOK_SECRET_PROVIDED'

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = AUTH_PIPELINE

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'

}
