# Generated by Django 4.0.6 on 2022-07-26 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0002_rename_product_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='ProductWeb',
            new_name='productWeb',
        ),
    ]
