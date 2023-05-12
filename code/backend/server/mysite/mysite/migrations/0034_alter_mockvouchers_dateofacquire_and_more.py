# Generated by Django 4.1.7 on 2023-05-12 12:48

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0033_alter_mockvouchers_dateofacquire_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mockvouchers',
            name='dateOfAcquire',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 12, 15, 48, 1, 315857)),
        ),
        migrations.AlterField(
            model_name='mockvouchers',
            name='dateOfExpiry',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 12, 15, 48, 1, 315857)),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='dateOfAcquire',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 12, 15, 48, 1, 314853)),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='dateOfExpiry',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
