# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-10 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0033_auto_20190109_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.FileField(default=11, upload_to='media'),
            preserve_default=False,
        ),
    ]
