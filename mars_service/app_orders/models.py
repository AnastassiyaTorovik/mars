from django.db import models
from datetime import datetime


class Device(models.Model):
    class Meta:
        db_table = 'devices'
        verbose_name = 'available devices'
        verbose_name_plural = 'available devices'
        constraints = [models.UniqueConstraint(fields=['manufacturer', 'model'], name='unique_device')]

    manufacturer = models.TextField(verbose_name='device manufacturer')
    model = models.TextField(verbose_name='device model')

    def __str__(self):
        return f'{self.manufacturer} {self.model}'


class Customer(models.Model):
    class Meta:
        db_table = 'customers'
        verbose_name = 'customer details'
        verbose_name_plural = 'customers\' details'

    customer_name = models.TextField()
    customer_registration_no = models.IntegerField(unique=True, null=True, default=None)
    customer_address = models.TextField()
    customer_city = models.TextField()

    def __str__(self):
        return self.customer_name


class DeviceInField(models.Model):
    class Meta:
        db_table = 'devices_in_fields'
        constraints = [models.UniqueConstraint(fields=['serial_number', 'analyzer'], name='unique_device_in_field')]

    serial_number = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    analyzer = models.ForeignKey(Device, on_delete=models.RESTRICT)
    owner_status = models.TextField()

    def __str__(self):
        return f'{self.serial_number} {self.analyzer} for {self.customer}'


class Order(models.Model):
    class Meta:
        db_table = 'orders'

    statuses = (('open', 'open'), ('closed', 'closed'), ('in progress', 'in progress'), ('need info', 'need info'))

    device = models.ForeignKey(DeviceInField, on_delete=models.RESTRICT)
    order_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateField(blank=True, null=True)
    order_status = models.TextField(choices=statuses)

    def save(self, *args, **kwargs):
        self.last_updated_at = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'order number {self.id} for {self.device}'

