# Generated by Django 2.1.7 on 2019-03-03 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icici', '0005_auto_20190303_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditupi',
            name='pin',
            field=models.IntegerField(default=7979),
        ),
    ]
