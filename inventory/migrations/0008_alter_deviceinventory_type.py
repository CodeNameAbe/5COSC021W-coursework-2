# Generated by Django 5.0.6 on 2024-06-20 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_deviceinventory_cpu_alter_deviceinventory_gpu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceinventory',
            name='type',
            field=models.CharField(max_length=50),
        ),
    ]