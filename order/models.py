"""Модуль моделей"""
from django.db import models


class Order(models.Model):
    """Модель заказа"""
    date = models.DateField(auto_now_add=True)
    comment = models.CharField(
        max_length=150,
        verbose_name='Текст заказа'
    )
    amount = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name='Сумма'
    )

    def __str__(self):
        return '{}'.format(self.id)
