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
            name='BlogConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('commentson', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200, db_index=True, verbose_name='Category title', unique=True)),
                ('description', models.TextField(max_length=500, verbose_name='Category Detail', blank=True, default='')),
                ('created', models.DateTimeField(verbose_name='Created On', auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified On')),
                ('slug', models.SlugField()),
            ],
            options={
                'db_table': 'blog_category',
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=240, db_index=True, verbose_name='Post title', unique=True)),
                ('shortdescription', models.TextField(max_length=400, verbose_name='Short Introduction')),
                ('content', models.TextField(verbose_name='Post HTML content')),
                ('status', models.SmallIntegerField(verbose_name='Post publish status', choices=[(0, 'Draft'), (1, 'Pending'), (2, 'Published'), (3, 'Archived')], default=0)),
                ('accesstype', models.SmallIntegerField(verbose_name='Post public access ', choices=[(0, 'Publically Accessible'), (1, 'Limited Access')], default=0)),
                ('commentenabled', models.BooleanField(default=True)),
                ('publisheddate', models.DateTimeField(verbose_name='Published Date ', blank=True, null=True)),
                ('created', models.DateTimeField(verbose_name='Created on', auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='blog.Category')),
            ],
            options={
                'db_table': 'blog_post',
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostMetta',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('metakey', models.CharField(max_length=200)),
                ('metavalue', models.TextField(max_length=500)),
                ('post', models.ForeignKey(to='blog.Post')),
            ],
            options={
                'db_table': 'blog_post_metatags',
                'verbose_name': 'Post Meta Tags',
                'verbose_name_plural': 'Post Meta Tags',
                'ordering': ['metakey'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200, db_index=True, verbose_name='Tag Name', unique=True)),
                ('description', models.TextField(max_length=400, verbose_name='Tag description', blank=True, default='')),
                ('created', models.DateTimeField(verbose_name='Created on', auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('slug', models.SlugField()),
            ],
            options={
                'db_table': 'blog_tag',
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tag',
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
    ]
