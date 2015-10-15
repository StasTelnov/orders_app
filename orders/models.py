from django.db import models
from django.conf import settings
from djmoney.models.fields import MoneyField


# Create your models here.
class Order(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='my_orders')
    executor = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='executed_orders')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
