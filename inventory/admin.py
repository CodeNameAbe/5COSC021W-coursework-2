from django.contrib import admin
from . models import DeviceInventory, MainInventory, Type

# Register your models here.
admin.site.register(DeviceInventory)
admin.site.register(MainInventory)
admin.site.register(Type)
