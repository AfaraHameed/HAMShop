# Generated by Django 4.1.4 on 2023-03-09 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0002_items_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartlist',
            name='razor_pay_order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cartlist',
            name='razor_pay_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cartlist',
            name='razor_pay_payment_signature',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
