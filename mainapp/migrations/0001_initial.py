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
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('initials', models.CharField(unique=True, max_length=10, default='BR')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('address', models.CharField(max_length=200)),
                ('zip', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('country', models.ForeignKey(to='mainapp.Country')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('address_line', models.CharField(max_length=1000)),
                ('order_weight', models.IntegerField(max_length=1000)),
                ('price', models.IntegerField(max_length=1000)),
                ('user', models.ForeignKey(to='mainapp.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=200)),
                ('weight', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(to='mainapp.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
