from django.views import generic
from django.shortcuts import redirect
from django.contrib import messages
from django.db import transaction
from django.conf import settings
from .models import Order
from libs.paginator import CustomPaginator


class IndexView(generic.ListView):
    paginator_class = CustomPaginator
    model = Order
    template_name = 'orders/index.html'
    paginate_by = 5
    ordering = '-created_at'
    queryset = Order.objects.select_related('customer') \
                            .filter(executor_id=None)


@transaction.atomic
def execute(request, pk):
    try:
        order = Order.objects.select_for_update().get(pk=pk, executor_id=None)
    except Order.DoesNotExist:
        messages.error(request, "While you are thinking the order was made.")
    else:
        request.user.balance.amount += \
            order.price.amount * (1 - settings.SYSTEM_FEE)
        order.executor = request.user
        order.save()
        request.user.save()
        messages.success(request,
                         "The order '%s' was successfully made." % order.title)
    finally:
        to = request.META.get('HTTP_REFERER', None) or '/'
        return redirect(to)
