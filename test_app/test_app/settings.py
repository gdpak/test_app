from os.path                  import join
from os.path                  import abspath
from os.path                  import dirname
from django.utils.translation import ugettext_lazy as _


DEBUG            = True
BASE_DIR         = dirname(dirname(abspath(__file__)))
SECRET_KEY       = '7y)xhk23$%lv@5sukzt*rdvm&py+!j3y*7(ex%u7+^h8f*7==*'
ROOT_URLCONF     = 'test_app.urls'
ALLOWED_HOSTS    = []
WSGI_APPLICATION = 'test_app.wsgi.application'

def getpath(resource_path):
    return abspath(join(BASE_DIR, resource_path))

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'suit',
    'gunicorn',
    'localflavor',
    'easy_thumbnails',

    'user_management',
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
]}}]

DATABASES = {
    'default': {
        'NAME'    : 'test',
        'PORT'    : '5432',
        'USER'    : 'postgres',
        'HOST'    : 'localhost',
        'ENGINE'  : 'django.db.backends.postgresql_psycopg2',
        'PASSWORD': '',
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

MEDIA_ROOT    = getpath('../media')
STATIC_ROOT   = getpath('../static')
LOCALE_PATHS  = (getpath('locale'),)
TEMPLATE_DIRS = (getpath('templates'),)

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

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
        'console'      : {'level': 'ERROR', 'class': 'logging.StreamHandler'             , 'formatter': 'semi_verbose'},
        'mail_admins'  : {'level': 'ERROR', 'class': 'django.utils.log.AdminEmailHandler', 'formatter': 'semi_verbose', 'filters' : ['require_debug_false']},
    },
    'loggers': {
        'django'        : {'level': 'DEBUG', 'handlers' : ['console', 'mail_admins'], 'propagate': False},
        'django.request': {'level': 'ERROR', 'handlers' : ['mail_admins'           ], 'propagate': False},
}}

SUIT_CONFIG = {
    'VERSION'                : "0.1",
    'ADMIN_NAME'             : _('Test App'),
    'SEARCH_URL'             : '/admin/user_management/user_information',
    'LIST_PER_PAGE'          : 30,
    'HEADER_DATE_FORMAT'     : 'l, j. F Y',
    'HEADER_TIME_FORMAT'     : 'H:i',
    'MENU_OPEN_FIRST_CHILD'  : True,
    'SHOW_REQUIRED_ASTERISK' : True,
    'CONFIRM_UNSAVED_CHANGES': True,
    'MENU': (
        '-',
        {'label': _('Operations'), 'icon': 'icon-briefcase' , 'models': ('artemis.partner', 'artemis.activity', 'artemis.activityobserveridentity'                    )},
        {'label': _('Forms'     ), 'icon': 'icon-tasks'     , 'models': ('artemis.form', 'artemis.formtype', 'artemis.formgroup', 'artemis.formfield'                 )},
        {'label': _('Results'   ), 'icon': 'icon-inbox'     , 'models': ('artemis.formfieldresult', 'artemis.formgroupresult', 'artemis.formresult'                   )},
        {'label': _('Observers' ), 'icon': 'icon-eye-open'  , 'models': ('artemis.observer', 'artemis.observerrole'                                                   )},
        {'label': _('Locations' ), 'icon': 'icon-map-marker', 'models': ('artemis.location', 'artemis.locationtype', 'artemis.pollingstation', 'artemis.pollingcenter')},
        {'label': _('Contacts'  ), 'icon': 'icon-bullhorn'  , 'models': ('artemis.phone', 'artemis.email' , 'artemis.address'                                         )},
        '-',
        {'label': _('Documentation'), 'icon': 'icon-question-sign', 'url': '/static/documentation/index.html'}
    ),
}
