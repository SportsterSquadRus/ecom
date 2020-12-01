"""Модуль форм"""
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """Form definition for Order."""

    class Meta:
        """Meta definition for Orderform."""

        model = Order
        fields = ('comment', 'amount')

        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
        }
