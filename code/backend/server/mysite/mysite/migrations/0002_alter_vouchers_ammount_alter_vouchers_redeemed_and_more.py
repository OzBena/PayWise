# Generated by Django 4.1.7 on 2023-04-11 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vouchers',
            name='ammount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='redeemed',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='storeType',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='voucherCategory',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='voucherID',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vouchers',
            name='walletID',
            field=models.IntegerField(),
        ),
    ]