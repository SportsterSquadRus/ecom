"""Модуль распределения url-адресов"""
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.OrdersListView.as_view(), name='order_list_url'),
]