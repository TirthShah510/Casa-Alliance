# Generated by Django 2.1.5 on 2019-02-14 09:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0071_auto_20190214_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_by', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('published_date', models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 13, 52, 600344, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 13, 52, 584346, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 13, 52, 584346, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 13, 52, 584346, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 13, 52, 576349, tzinfo=utc)),
        ),
    ]
