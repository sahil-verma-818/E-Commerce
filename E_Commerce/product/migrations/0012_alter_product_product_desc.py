# Generated by Django 4.2.7 on 2023-12-11 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_product_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.CharField(max_length=600),
        ),
    ]