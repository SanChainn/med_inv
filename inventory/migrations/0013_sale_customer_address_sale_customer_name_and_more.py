# Generated by Django 5.2.3 on 2025-06-29 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_sale_delivery_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='customer_address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sale',
            name='customer_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='sale',
            name='customer_phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
