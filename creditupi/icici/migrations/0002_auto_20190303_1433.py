# Generated by Django 2.1.7 on 2019-03-03 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('icici', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditUpi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('mobile_no', models.IntegerField()),
                ('pin', models.IntegerField()),
                ('status', models.CharField(max_length=1)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(max_length=1)),
                ('trans_key', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('credit_upi_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icici.CreditUpi')),
            ],
        ),
        migrations.AlterField(
            model_name='upi',
            name='virtual_address',
            field=models.CharField(max_length=50),
        ),
    ]
