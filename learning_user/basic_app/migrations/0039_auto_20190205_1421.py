# Generated by Django 2.1.5 on 2019-02-05 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0038_auto_20190205_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintpost',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
