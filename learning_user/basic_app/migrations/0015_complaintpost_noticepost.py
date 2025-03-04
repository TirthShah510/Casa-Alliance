# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-25 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0014_auto_20181225_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_subject', models.CharField(max_length=64)),
                ('complaint_description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='NoticePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_subject', models.CharField(max_length=64)),
                ('notice_description', models.TextField(max_length=500)),
            ],
        ),
    ]
