# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150524_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='date_of_join',
            new_name='date_joined',
        ),
    ]
