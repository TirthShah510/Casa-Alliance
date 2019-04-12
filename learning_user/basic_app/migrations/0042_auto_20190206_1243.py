# Generated by Django 2.1.5 on 2019-02-06 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0041_property_registered_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='id',
            field=models.AutoField(auto_created=True, default=11, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='wing_name',
            field=models.CharField(max_length=64),
        ),
    ]
