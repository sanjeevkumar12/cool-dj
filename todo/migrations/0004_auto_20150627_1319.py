# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20150616_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='slug',
            field=models.SlugField(unique=True, blank=True, max_length=254),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='slug',
            field=models.SlugField(blank=True, max_length=254),
            preserve_default=True,
        ),
    ]
