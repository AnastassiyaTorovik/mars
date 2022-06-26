from django.contrib import admin
from .models import Order, Customer, Device, DeviceInField


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer', 'model')
    search_fields = ('manufacturer', 'model')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    def my_customer(self, obj):
        return obj.device.customer.customer_name

    def my_device_model(self, obj):
        return obj.device.analyzer.model

    def my_device_manufacturer(self, obj):
        return obj.device.analyzer.manufacturer

    def my_serial_number(self, obj):
        return obj.device.serial_number

    my_customer.short_description = 'Customer'
    my_device_model.short_description = 'Device Model'
    my_device_manufacturer.short_description = 'Device Manufacturer'
    my_serial_number.short_description = 'Serial Number'

    list_display = ('id', 'my_customer', 'my_device_model', 'my_device_manufacturer', 'my_serial_number',
                    'order_description', 'created_at', 'last_updated_at', 'order_status')

    search_fields = ('device__customer__customer_name', 'device__id', 'device__serial_number',
                     'device__analyzer__model', 'device__analyzer__manufacturer')
    raw_id_fields = ('device', )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_address', 'customer_city')
    search_fields = ('customer_name', 'customer_address')


@admin.register(DeviceInField)
class DeviceInFieldAdmin(admin.ModelAdmin):
    def my_customer(self, obj):
        return obj.customer.customer_name

    def my_device_model(self, obj):
        return obj.analyzer.model

    def my_device_manufacturer(self, obj):
        return obj.analyzer.manufacturer

    my_customer.short_description = 'Customer'
    my_device_model.short_description = 'Device Model'
    my_device_manufacturer.short_description = 'Device Manufacturer'

    list_display = ('id', 'serial_number', 'my_customer', 'my_device_model', 'my_device_manufacturer', 'owner_status')
    search_fields = ('serial_number', )
    raw_id_fields = ('customer', 'analyzer')
