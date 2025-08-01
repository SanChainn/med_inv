# Generated by Django 5.2.3 on 2025-06-29 07:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_remove_medicine_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.medicinetype', verbose_name='Category'),
        ),
    ]
