# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-26 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0019_auto_20181225_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(max_length=64)),
                ('total_members', models.PositiveIntegerField()),
                ('house_name', models.CharField(blank=True, max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='society',
            name='flat_no',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='society',
            name='wing_name',
            field=models.CharField(default=11, max_length=64),
            preserve_default=False,
        ),
    ]
