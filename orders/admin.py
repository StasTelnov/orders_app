from django.contrib import admin
from .models import Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    exclude = ('customer', 'executor',)

    def save_model(self, request, obj, form, change):
        obj.customer = request.user
        obj.save()

admin.site.register(Order, OrderAdmin)
