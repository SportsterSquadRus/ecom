"""Модуль обработки запросов"""
from django.views.generic import ListView
from .models import Order

class OrdersListView(ListView):
    """Вывод всех заказов"""
    model = Order
    queryset = Order.objects.all()
    template_name = "order/order_list.html"
    context_object_name = 'orders'
    paginate_by = 4
