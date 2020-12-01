"""Модуль обработки запросов"""
from django.views.generic import ListView, CreateView, DetailView, UpdateView, View, DeleteView
from django.shortcuts import render, redirect, reverse
from .models import Order
from .forms import OrderForm, FilterForm
from django.urls import reverse_lazy


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list_url')


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
    template_name = 'order/order_create.html'


class OrderDetailView(DetailView):
    """Детальная информация о заказе"""
    model = Order
    template_name = 'order/order_detail.html'
    context_object_name = 'order'


class OrderUpdateView(UpdateView):
    """Изменение заказа"""
    model = Order
    template_name = 'order/order_create.html'
    form_class = OrderForm


class FilterFormView(ListView):
    paginate_by = 4
    template_name = "order/order_list.html"
    context_object_name = 'orders'

    def get_queryset(self):
        start = self.request.GET.get('start')
        stop = self.request.GET.get('stop')
        if not start:
            start = "1900-01-01"
        if not stop:
            stop = "2100-01-01"
        return Order.objects.filter(date__range=[start, stop])

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['start'] = self.request.GET.get('start')
    #     context['stop'] = self.request.GET.get('stop')
    #     return context
