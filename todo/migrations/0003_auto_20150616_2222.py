# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20150614_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasklist',
            name='slug',
            field=models.SlugField(unique=True, default='s', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todoitem',
            name='slug',
            field=models.SlugField(default='s', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='tasklist',
            unique_together=set([('title', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='todoitem',
            unique_together=set([('title', 'todolist')]),
        ),
    ]
