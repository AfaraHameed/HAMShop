# Generated by Django 4.1.4 on 2023-03-15 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0002_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]