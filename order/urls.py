"""Модуль распределения url-адресов"""
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.OrdersListView.as_view(), name='order_list_url'),
    path('create/', views.OrderCreateView.as_view(), name='order_create_url'),
    path('detail/<int:pk>/', views.OrderDetailView.as_view(),name='order_detail_url'),
    path('update/<int:pk>/', views.OrderUpdateView.as_view(),name='order_update_url'),
    path('filter/', views.FilterFormView.as_view(), name='filter_form_url')
]