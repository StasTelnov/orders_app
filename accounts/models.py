from django.contrib.auth.models import AbstractUser
from djmoney.models.fields import MoneyField


class CustomUser(AbstractUser):
    balance = MoneyField(max_digits=10, decimal_places=2,
                         default_currency='USD')
