# Generated by Django 4.2.7 on 2023-11-30 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_status_order_total_bill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
    ]