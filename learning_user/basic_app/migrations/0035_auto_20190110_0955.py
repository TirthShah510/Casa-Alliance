# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-10 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0034_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
