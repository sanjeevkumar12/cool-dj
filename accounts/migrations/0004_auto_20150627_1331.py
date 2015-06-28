# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150524_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True, max_length=254),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='user_hash',
            field=models.CharField(default='', blank=True, max_length=254),
            preserve_default=True,
        ),
    ]
