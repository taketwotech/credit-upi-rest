# Generated by Django 2.1.7 on 2019-03-06 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icici', '0011_auto_20190306_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditupi',
            name='limit',
            field=models.IntegerField(default=6000),
        ),
        migrations.AlterField(
            model_name='creditupi',
            name='pin',
            field=models.IntegerField(default=3514),
        ),
    ]