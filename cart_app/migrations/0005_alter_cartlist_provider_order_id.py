# Generated by Django 4.1.4 on 2023-03-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0004_cartlist_provider_order_id_cartlist_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartlist',
            name='provider_order_id',
            field=models.CharField(max_length=40, verbose_name='Order ID'),
        ),
    ]