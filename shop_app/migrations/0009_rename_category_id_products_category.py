# Generated by Django 3.2.15 on 2022-11-21 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0008_auto_20221116_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category_id',
            new_name='category',
        ),
    ]