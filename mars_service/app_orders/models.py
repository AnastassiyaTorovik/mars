from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy


class Device(models.Model):
    class Meta:
        db_table = 'devices'
        verbose_name = 'available devices'
        verbose_name_plural = 'available devices'

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
    customer_address = models.TextField()
    customer_city = models.TextField()

    def __str__(self):
        return self.customer_name


class DeviceInField(models.Model):
    class Meta:
        db_table = 'devices_in_fields'

    serial_number = models.TextField()
    customer_id = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    analyzer_id = models.ForeignKey(Device, on_delete=models.RESTRICT)
    owner_status = models.TextField()


def status_validator(order_status):
    if order_status not in ['open', 'closed', 'in progress', 'need info']:
        raise ValidationError(
            gettext_lazy('%(order_status)s is wrong order status',
                         params={'order_status': order_status})
        )


class Order(models.Model):
    class Meta:
        db_table = 'orders'

    device = models.ForeignKey(DeviceInField, on_delete=models.RESTRICT)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    order_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateField(blank=True, null=True)
    order_status = models.TextField(validators=[])

    def save(self, *args, **kwargs):
        self.last_updated_at = datetime.now()
        super().save(*args, **kwargs)

