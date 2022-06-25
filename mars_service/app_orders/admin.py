from django.contrib import admin
from .models import Order, Customer, Device, DeviceInField


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer', 'model')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('device', 'customer', 'order_description', 'created_at', 'last_updated_at', 'order_status')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_address', 'customer_city')


@admin.register(DeviceInField)
class DeviceInFieldAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'customer_id', 'analyzer_id', 'owner_status')