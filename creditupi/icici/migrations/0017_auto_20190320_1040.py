# Generated by Django 2.1.7 on 2019-03-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icici', '0016_auto_20190319_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='creditupi',
            name='limit',
            field=models.IntegerField(default=7000),
        ),
        migrations.AlterField(
            model_name='creditupi',
            name='pin',
            field=models.IntegerField(default=7930),
        ),
    ]
