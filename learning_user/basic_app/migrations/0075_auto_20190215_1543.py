# Generated by Django 2.1.5 on 2019-02-15 10:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0074_auto_20190214_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=64)),
                ('servant', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('service', models.CharField(choices=[('Housekeeper', 'Housekeeper'), ('Cook', 'Cook'), ('Head Nurse/Nanny', 'Head Nurse/Nanny'), ('Housemaid/Cleaner', 'Housemaid/Cleaner'), ('Laundry', 'Laundry'), ('Gardener', 'Gardener'), ('Dairymaid', 'Dairymaid'), ('Others', 'Others')], max_length=30)),
                ('full_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=64)),
                ('type', models.CharField(choices=[('MotorCycle', 'MotorCycle'), ('Car', 'Car'), ('Bicycle', 'Bicycle')], max_length=10)),
                ('number', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='profile',
            name='staff',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='vehicles',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], default=1111),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 10, 12, 10, 667666, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commentadd',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 10, 12, 10, 671659, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 10, 12, 10, 649206, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 10, 12, 10, 649206, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
