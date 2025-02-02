# Generated by Django 5.0.6 on 2024-06-21 01:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0017_remove_deviceinventory_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.CreateModel(
            name='MainInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('audit', models.DateField()),
                ('location', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('available', 'Available'), ('on rent', 'On Rent'), ('dismantle', 'Dismantle')], default='available', max_length=50)),
                ('borrow_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField()),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'MainInventory',
            },
        ),
        migrations.CreateModel(
            name='DeviceInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('serial', models.CharField(max_length=200)),
                ('cpu', models.CharField(max_length=200)),
                ('gpu', models.CharField(max_length=200)),
                ('ram', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.type')),
            ],
            options={
                'verbose_name_plural': 'DeviceInventory',
            },
        ),
    ]
