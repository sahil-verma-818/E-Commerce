# Generated by Django 4.2.7 on 2023-11-21 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_brand_color_mdl_product_brand_product_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]
