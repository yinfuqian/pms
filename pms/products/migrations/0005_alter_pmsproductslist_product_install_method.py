# Generated by Django 4.2.2 on 2023-07-19 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_product_nodes_pmsproductslist_product_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pmsproductslist',
            name='product_install_method',
            field=models.CharField(default='未知', max_length=50, null=True, verbose_name='部署方式'),
        ),
    ]
