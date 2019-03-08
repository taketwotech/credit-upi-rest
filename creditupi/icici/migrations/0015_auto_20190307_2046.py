# Generated by Django 2.1.7 on 2019-03-07 20:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('icici', '0014_auto_20190307_2022'),
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
            field=models.IntegerField(default=4095),
        ),
        migrations.AlterUniqueTogether(
            name='beneficiary',
            unique_together={('author', 'vpa')},
        ),
    ]
