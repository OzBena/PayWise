# Generated by Django 4.1.7 on 2023-04-14 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_alter_vouchers_dateofacquire_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vouchers',
            name='dateOfAcquire',
            field=models.CharField(default='undefined', max_length=30),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='dateOfExpiry',
            field=models.CharField(default='undefined', max_length=30),
        ),
    ]
