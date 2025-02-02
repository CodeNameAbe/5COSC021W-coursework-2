# Generated by Django 5.0.6 on 2024-06-20 23:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_alter_maininventory_name_alter_maininventory_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininventory',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_inventory_name', to='inventory.deviceinventory'),
        ),
        migrations.AlterField(
            model_name='maininventory',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_inventory_type', to='inventory.deviceinventory'),
        ),
    ]
