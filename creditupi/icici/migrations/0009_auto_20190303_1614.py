# Generated by Django 2.1.7 on 2019-03-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icici', '0008_auto_20190303_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditupi',
            name='limit',
            field=models.IntegerField(default=10000),
        ),
        migrations.AlterField(
            model_name='creditupi',
            name='pin',
            field=models.IntegerField(default=1899),
        ),
    ]
