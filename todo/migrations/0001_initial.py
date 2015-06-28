# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=244, verbose_name='Task List Name', db_index=True)),
                ('description', models.TextField(max_length=500, verbose_name='List Description')),
                ('created', models.DateTimeField(verbose_name='Created', auto_now_add=True)),
                ('userid', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=244, verbose_name='Task Name', db_index=True)),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('status', models.IntegerField(default=1, verbose_name='Task Status', choices=[(0, 'Draft'), (1, 'Pending'), (2, 'In-Progress'), (3, 'Complete'), (4, 'On-Hold')])),
                ('priority', models.IntegerField(default=0, verbose_name='Priority', choices=[(0, 'Normal'), (1, 'Medium'), (2, 'High'), (3, 'Critial')])),
                ('duedatetime', models.DateTimeField(verbose_name='Due Date', blank=True)),
                ('created', models.DateTimeField(verbose_name='Created', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Last Modified', auto_now=True)),
                ('todolist', models.ForeignKey(to='todo.TaskList')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
