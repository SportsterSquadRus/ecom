"""Модуль форм"""
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """Форма создания и редактирования заказа"""

    class Meta:
        """Настройки формы"""

        model = Order
        fields = ('agent', 'comment', 'amount', 'date')

        widgets = {
            'agent': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
