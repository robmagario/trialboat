# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('initials', models.CharField(default='BR', max_length=10, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('family_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('zip', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=20)),
                ('country', models.ForeignKey(to='mainapp.Country')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('weight', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(to='mainapp.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
