# Generated by Django 3.2.15 on 2022-11-15 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_auto_20221115_2246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category',
            new_name='category_id',
        ),
        migrations.RemoveField(
            model_name='products',
            name='review',
        ),
        migrations.RemoveField(
            model_name='products',
            name='star',
        ),
    ]
