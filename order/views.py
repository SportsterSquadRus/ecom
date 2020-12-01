"""Модуль обработки запросов"""
from django.views.generic import ListView, CreateView, DetailView
from .models import Order
from .forms import OrderForm
# from django.shortcuts import redirect, reverse

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
    # success_url = '/'
    template_name = 'order/order_create.html'

class OrderDetailView(DetailView):
    """Детальная информация о заказе"""
    model = Order
    template_name = 'order/order_detail.html'
    context_object_name = 'order'
