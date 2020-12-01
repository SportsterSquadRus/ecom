"""Модуль форм"""
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """Form definition for Order."""

    class Meta:
        """Meta definition for Orderform."""

        model = Order
        fields = ('comment', 'amount', 'date')

        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_amount(self):
        if not self.cleaned_data['amount']:
            raise forms.ValidationError(
                "Введите значение.")
        return self.cleaned_data['amount']


class FilterForm(forms.Form):
    date_left = forms.DateField(label='С...')
    date_right = forms.DateField(label='По...')
