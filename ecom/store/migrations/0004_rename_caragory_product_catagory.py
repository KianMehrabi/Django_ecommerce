# Generated by Django 4.2.15 on 2024-08-27 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='caragory',
            new_name='catagory',
        ),
    ]
