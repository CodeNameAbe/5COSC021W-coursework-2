# Generated by Django 5.0.6 on 2024-06-21 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_alter_deviceinventory_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceinventory',
            name='user',
        ),
        migrations.RemoveField(
            model_name='maininventory',
            name='user',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.DeleteModel(
            name='DeviceInventory',
        ),
        migrations.DeleteModel(
            name='MainInventory',
        ),
    ]
