# Generated by Django 5.0.6 on 2024-06-20 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_remove_deviceinventory_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceinventory',
            name='cpu',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='deviceinventory',
            name='gpu',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='deviceinventory',
            name='ram',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='deviceinventory',
            name='serial',
            field=models.CharField(max_length=200),
        ),
    ]
