# Generated by Django 4.1.4 on 2023-03-14 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0003_cartlist_razor_pay_order_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartlist',
            name='provider_order_id',
            field=models.CharField(default='null', max_length=40),
        ),
        migrations.AddField(
            model_name='cartlist',
            name='status',
            field=models.CharField(default='Pending', max_length=254),
        ),
    ]
