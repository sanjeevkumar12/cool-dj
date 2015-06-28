# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20150627_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hash_expire',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 27, 8, 2, 54, 687640, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
