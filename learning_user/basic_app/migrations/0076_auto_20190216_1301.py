# Generated by Django 2.1.5 on 2019-02-16 07:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0075_auto_20190215_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 16, 7, 31, 15, 219823, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commentadd',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 16, 7, 31, 15, 229824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='staff',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='vehicles',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_balconies',
            field=models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 16, 7, 31, 15, 207452, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 16, 7, 31, 15, 207452, tzinfo=utc)),
        ),
    ]
