# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, verbose_name='Email Address', max_length=75, db_index=True)),
                ('firstname', models.CharField(null=True, verbose_name='First Name', max_length=20, blank=True)),
                ('lastname', models.CharField(null=True, verbose_name='Last Name', max_length=20, blank=True)),
                ('user_bio', models.TextField(null=True, verbose_name='User Intro', blank=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is staff user')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('dateofjoin', models.DateTimeField(auto_now_add=True, verbose_name='Joined Time')),
                ('image', models.ImageField(null=True, verbose_name='User Image', upload_to='uploads/users/profile/', default='uploads/users/profile   /noimage.png', blank=True)),
                ('avatar', models.ImageField(null=True, verbose_name='User Image', upload_to='uploads/users/avatar/', default='uploads/users/avatar/noimage.png', blank=True)),
                ('groups', models.ManyToManyField(to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups', related_name='user_set', related_query_name='user', blank=True)),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', help_text='Specific permissions for this user.', verbose_name='user permissions', related_name='user_set', related_query_name='user', blank=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
    ]
