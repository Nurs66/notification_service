import pytz
from django.db import models

from utils.validators import phone_number_regex


class Customer(models.Model):
    phone_number = models.CharField(
        max_length=13,
        validators=[phone_number_regex],
        verbose_name='Phone number'
    )
    mobile_operator_code = models.CharField(
        max_length=13,
        verbose_name='Mobile operator code'
    )
    timezone = models.CharField(
        max_length=50,
        default='UTC',
        choices=[(tz, tz) for tz in pytz.all_timezones]
    )
    tag = models.CharField(
        max_length=100,
        verbose_name='Search tags',
    )

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ('-id',)

    def __str__(self):
        return f"{self.phone_number} -- {self.timezone}"
