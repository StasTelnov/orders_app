from django.views import generic
from .models import Order


class IndexView(generic.ListView):
    model = Order
    template_name = 'orders/index.html'
    # context_object_name = 'orders'
    paginate_by = 10
    ordering = '-created_at'
