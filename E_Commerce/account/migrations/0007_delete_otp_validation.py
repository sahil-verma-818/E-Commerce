# Generated by Django 4.2.7 on 2024-01-05 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_otp_validation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='otp_validation',
        ),
    ]