# Generated by Django 4.0.6 on 2022-07-26 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0003_rename_productweb_products_productweb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='productWeb',
            new_name='ProductWeb',
        ),
    ]
