from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DeviceInventory(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, blank=True, null=True)
    serial = models.CharField(max_length=200)
    cpu = models.CharField(max_length=200)
    gpu = models.CharField(max_length=200)
    ram = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'DeviceInventory'

    def __str__(self):
        return self.name


class MainInventory(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField()
    audit = models.DateField()
    location = models.CharField(max_length=50)
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('on rent', 'On Rent'),
        ('dismantle', 'Dismantle'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='available')
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    class Meta:
        verbose_name_plural = 'MainInventory'
    
    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Types'

    def __str__(self):
        return self.name