# Generated by Django 5.2.3 on 2025-06-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_medicine_price_medicine_batch_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Threshold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('low_stock_threshold', models.PositiveIntegerField(default=10, help_text='Quantity at or below which a medicine is considered low stock.')),
                ('expiry_threshold_days', models.PositiveIntegerField(default=30, help_text="Number of days within which a medicine is considered 'expiring soon'.")),
            ],
            options={
                'verbose_name_plural': 'Thresholds',
            },
        ),
    ]
