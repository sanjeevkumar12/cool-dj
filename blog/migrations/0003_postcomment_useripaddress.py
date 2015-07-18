# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150718_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='useripaddress',
            field=models.IPAddressField(blank=True, default=False),
            preserve_default=True,
        ),
    ]
