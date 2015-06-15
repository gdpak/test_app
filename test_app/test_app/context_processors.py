from django.conf import settings


def global_settings(request):
    return {
        'AVATAR_SIZE'       : settings.AVATAR_SIZE       ,
        'APPLICATION_NAME'  : settings.APPLICATION_NAME  ,
        'DEFAULT_AVATAR_URL': settings.DEFAULT_AVATAR_URL,
    }
