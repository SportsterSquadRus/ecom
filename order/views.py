"""Модуль обработки запросов"""
from django.views.generic import ListView, CreateView
from .models import Order
from .forms import OrderForm

class OrdersListView(ListView):
    """Вывод всех заказов"""
    model = Order
    queryset = Order.objects.all()
    template_name = "order/order_list.html"
    context_object_name = 'orders'
    paginate_by = 4

class OrderCreateView(CreateView):
    """Создание заказа"""
    model = Order
    form_class = OrderForm
    success_url = '/'
    template_name = 'order/order_create.html'
