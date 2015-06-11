# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from six                        import string_types
from django.db                  import migrations
from django.contrib.auth.models import User


def get_default_settings(config_name, data_type=string_types):
    from django.conf import settings

    if hasattr(settings, config_name):
        config_value = settings.gettar(config_name)
        if isinstance(config_value, data_type):
            return config_value

def create_superuser(*args, **kwargs):
    superuser_email    = get_default_settings('DEFAULT_SUPERUSER_EMAIL'   )
    superuser_login    = get_default_settings('DEFAULT_SUPERUSER_LOGIN'   )
    superuser_password = get_default_settings('DEFAULT_SUPERUSER_PASSWORD')

    superuser_email    = superuser_email    or 'a@b.c'
    superuser_login    = superuser_login    or 'admin'
    superuser_password = superuser_password or 'admin'

    User.objects.create_superuser(
        email    = superuser_email,
        username = superuser_login,
        password = superuser_password)



class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
