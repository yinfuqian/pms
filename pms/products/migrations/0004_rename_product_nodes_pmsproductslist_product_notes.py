# Generated by Django 4.2.2 on 2023-07-19 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_pmsproductslist_product_nodes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pmsproductslist',
            old_name='product_nodes',
            new_name='product_notes',
        ),
    ]
