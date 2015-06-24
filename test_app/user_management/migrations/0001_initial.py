# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db   import models
from django.db   import migrations
from django.conf import settings

from django_iban.fields import IBANField


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id'             , models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture'        , models.ImageField(upload_to=b'%Y/%m/%d', verbose_name='Picture')),
                ('last_name'      , models.CharField(max_length=20, verbose_name='last name')),
                ('first_name'     , models.CharField(max_length=20, verbose_name='first name')),
                ('IBAN_account'   , IBANField(unique=True, enforce_database_constraint=True)),
                ('account_manager', models.ForeignKey(verbose_name='account manager', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name'       : 'User information',
                'verbose_name_plural': 'Users information',
            },
        ),
        migrations.AlterUniqueTogether(
            name            = 'userinformation',
            unique_together = set([('first_name', 'last_name')]),
        ),
    ]
