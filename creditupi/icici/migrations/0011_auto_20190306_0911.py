# Generated by Django 2.1.7 on 2019-03-06 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('icici', '0010_auto_20190305_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='creditupi',
            name='limit',
            field=models.IntegerField(default=10000),
        ),
        migrations.AlterField(
            model_name='creditupi',
            name='pin',
            field=models.IntegerField(default=2078),
        ),
    ]
