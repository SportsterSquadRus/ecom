"""Модуль моделей"""
from django.db import models
from django.shortcuts import reverse


class Order(models.Model):
    """Модель заказа"""
    date = models.DateField(verbose_name='Дата заказа')
    agent = models.CharField(max_length=100, verbose_name='Контрагент')
    comment = models.CharField(max_length=150, verbose_name='Текст заказа')
    amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Сумма заказа')

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('order_detail_url', kwargs={'pk': self.pk})

    def __str__(self):
        return '{}'.format(self.id)
