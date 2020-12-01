"""Модуль моделей"""
from django.db import models
from django.shortcuts import reverse


class Order(models.Model):
    """Модель заказа"""
    date = models.DateField()
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

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('order_detail_url', kwargs={'pk': self.pk})

    def __str__(self):
        return '{}'.format(self.id)
