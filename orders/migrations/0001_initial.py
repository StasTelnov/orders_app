# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import djmoney.models.fields
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('price_currency', djmoney.models.fields.CurrencyField(max_length=3, default='USD', editable=False, choices=[('USD', 'US Dollar')])),
                ('price', djmoney.models.fields.MoneyField(default_currency='USD', default=Decimal('0.0'), max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], decimal_places=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(related_name='my_orders', to=settings.AUTH_USER_MODEL)),
                ('executor', models.ForeignKey(blank=True, null=True, related_name='executed_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
