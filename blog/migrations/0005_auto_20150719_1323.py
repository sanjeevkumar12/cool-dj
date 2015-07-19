# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150718_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='email',
            field=models.EmailField(default='sdf', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postcomment',
            name='name',
            field=models.CharField(verbose_name='Posted By', default='sds', max_length=240),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='user',
            field=models.ForeignKey(default=None, blank=True, null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
