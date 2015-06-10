import os

DEBUG            = True
BASE_DIR         = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY       = '7y)xhk23$%lv@5sukzt*rdvm&py+!j3y*7(ex%u7+^h8f*7==*'
ROOT_URLCONF     = 'test_app.urls'
ALLOWED_HOSTS    = []
WSGI_APPLICATION = 'test_app.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'suit',
    'localflavor',
    'user_management',
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

TEMPLATES = [{
    'BACKEND' : 'django.template.backends.django.DjangoTemplates',
    'DIRS'    : [],
    'APP_DIRS': True,
    'OPTIONS' : {
        'context_processors': [
            'django.core.context_processors.request',
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'social.apps.django_app.context_processors.backends',
            'social.apps.django_app.context_processors.login_redirect',
]}}]

DATABASES = {
    'default': {
        'NAME'  : os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.sqlite3',
}}

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth',
    'social.backends.google.GoogleOAuth2',
)

USE_TZ        = True
USE_I18N      = True
USE_L10N      = True
TIME_ZONE     = 'UTC'
LANGUAGE_CODE = 'en-us'

MEDIA_URL   = '/media/'
STATIC_URL  = '/static/'
MEDIA_ROOT  = os.path.abspath(os.path.join(BASE_DIR, "../media" ))
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, "../static"))

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
