from __future__ import print_function

from os                       import environ
from json                     import loads
from base64                   import b64decode
from os.path                  import join
from os.path                  import abspath
from os.path                  import dirname
from django.utils.translation import ugettext_lazy as _


extra_configuration = loads(b64decode(environ['XANADOU_EXTRA_INFO']).decode('utf-8'))

DEBUG          = extra_configuration['debug']
TEMPLATE_DEBUG = DEBUG

BASE_DIR         = dirname(dirname(abspath(__file__)))
ROOT_URLCONF     = 'test_app.urls'
WSGI_APPLICATION = 'test_app.wsgi.application'

SECRET_KEY            = '7y)xhk23$%lv@5sukzt*rdvm&py+!j3y*7(ex%u7+^h8f*7==*'
ALLOWED_HOSTS         = [environ['XANADOU_SERVER_NAME']]
CSRF_COOKIE_SECURE    = True
SESSION_COOKIE_SECURE = True

APPLICATION_NAME  = environ['XANADOU_APP_NAME']
ACCOUNTS_PER_PAGE = 10

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

THUMBNAIL_ALIASES = {
    '': {
        'thumb'  : {'size': (50 ,  50), 'crop': False},
        'avatar' : {'size': (100, 100), 'crop': False},
        'preview': {'size': (150, 150), 'crop': False},
}}


def getpath(resource_path):
    return abspath(join(BASE_DIR, resource_path))

INSTALLED_APPS = (
    'suit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'gunicorn',
    'debug_toolbar',
    'rest_framework',
    'easy_thumbnails',
    'social.apps.django_app.default',

    'django_iban',
    'user_management',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
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
    'DIRS'    : [getpath('templates'),],
    'APP_DIRS': True,
    'OPTIONS' : {
        'context_processors': [
            'django.core.context_processors.request',
            'django.template.context_processors.debug',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',

            'test_app.context_processors.global_settings',
            'social.apps.django_app.context_processors.backends',
            'social.apps.django_app.context_processors.login_redirect',
]}}]

DATABASES = {
    'default': {
        'NAME'    : APPLICATION_NAME,
        'PORT'    : '5432',
        'USER'    : 'postgres',
        'HOST'    : '127.0.0.1',
        'ENGINE'  : 'django.db.backends.postgresql_psycopg2',
        'PASSWORD': '',
}}

USE_TZ        = True
USE_I18N      = True
USE_L10N      = True
TIME_ZONE     = 'UTC'
LANGUAGE_CODE = 'en-us'

MEDIA_URL          = '/media/'
STATIC_URL         = '/static/'
AVATAR_SIZE        = '150'
DEFAULT_AVATAR_URL = STATIC_URL + 'img/default_avatar.gif'

MEDIA_ROOT       = getpath('../media' )
STATIC_ROOT      = getpath('../static')
LOCALE_PATHS     = (getpath('locale'),)
STATICFILES_DIRS = (getpath('assets'),)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level'   : 'DEBUG',
        'handlers': ['console'],
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
    }},
    'formatters': {
        'semi_verbose': {
            'format': '[%(filename)s] [%(process)d]%(module)s %(funcName)s() : %(lineno)d: %(message)s'
    }},
    'handlers': {
        'console'      : {'level': 'DEBUG', 'class': 'logging.StreamHandler'             , 'formatter': 'semi_verbose'},
        'mail_admins'  : {'level': 'ERROR', 'class': 'django.utils.log.AdminEmailHandler', 'formatter': 'semi_verbose', 'filters' : ['require_debug_false']},
    },
    'loggers': {
        'django'        : {'level': 'DEBUG', 'handlers' : ['console', 'mail_admins'], 'propagate': False},
        'django.request': {'level': 'ERROR', 'handlers' : ['mail_admins'           ], 'propagate': False},
}}

SUIT_CONFIG = {
    'VERSION'                : "0.1",
    'ADMIN_NAME'             : _(APPLICATION_NAME.upper()),
    'SEARCH_URL'             : '/admin/user_management/userinformation/',
    'LIST_PER_PAGE'          : 30,
    'HEADER_DATE_FORMAT'     : 'l, j. F Y',
    'HEADER_TIME_FORMAT'     : 'H:i',
    'MENU_OPEN_FIRST_CHILD'  : True,
    'SHOW_REQUIRED_ASTERISK' : True,
    'CONFIRM_UNSAVED_CHANGES': True,
    'MENU': (
        '-',
        {'label': _('Authentication'), 'icon': 'icon-briefcase', 'models': ('auth.user', 'auth.group'        ,)},
        {'label': _('Management'    ), 'icon': 'icon-tasks'    , 'models': ('user_management.userinformation',)},
        '-',
        {'label': _('Documentation'), 'icon': 'icon-question-sign', 'url': '/static/documentation/index.html'}
    ),
}

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL          = '/login/'
LOGOUT_URL         = '/logout/'
LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY        = extra_configuration['google_oauth2_key'   ]
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET     = extra_configuration['google_oauth2_secret']
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details'    ,
    'social.pipeline.social_auth.social_uid'        ,
    'social.pipeline.social_auth.auth_allowed'      ,
    'social.pipeline.social_auth.social_user'       ,
    'social.pipeline.user.get_username'             ,
    'social.pipeline.user.create_user'              ,
    'social.pipeline.social_auth.associate_user'    ,
    'social.pipeline.social_auth.load_extra_data'   ,
    'social.pipeline.user.user_details'             ,
    'user_management.pipeline.add_avatar_to_session',
)

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_PATCH_SETTINGS = False

DEBUG_TOOLBAR_CONFIG = {
    'RENDER_PANELS'        : True,
    'DISABLE_PANELS'       : set(['debug_toolbar.panels.redirects.RedirectsPanel']),
    'SHOW_COLLAPSED'       : True,
    'ENABLE_STACKTRACES'   : True,
    'SHOW_TEMPLATE_CONTEXT': True,
    'SHOW_TOOLBAR_CALLBACK': lambda _: DEBUG,
    'DISABLE_PANELS'       : set(['debug_toolbar.panels.redirects.RedirectsPanel']),
    'JQUERY_URL'           : STATIC_URL + 'js/jquery.min.js',
}

CACHES = {
    'default': {
        'TIMEOUT' : None,
        'BACKEND' : 'redis_cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'OPTIONS' : {
            'MAX_ENTRIES'                 : 100,
            'PARSER_CLASS'                : 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS'       : 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'timeout'        : 60,
                'max_connections': 10,
}}}}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
