# Generated by Django 5.0.6 on 2024-06-21 01:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maininventory',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.type'),
        ),
    ]
