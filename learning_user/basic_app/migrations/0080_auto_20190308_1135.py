# Generated by Django 2.1.5 on 2019-03-08 06:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0079_auto_20190308_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 8, 6, 5, 12, 959924, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commentadd',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 8, 6, 5, 12, 959924, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='complaintpost',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 8, 6, 5, 12, 939923, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hall',
            name='registration_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 8, 6, 5, 12, 939923, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='noticepost',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 8, 6, 5, 12, 939923, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 8, 6, 5, 12, 949922, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 8, 6, 5, 12, 949922, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='date_and_time_out',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 8, 6, 5, 12, 949922, tzinfo=utc)),
        ),
    ]
