from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .models import Order
from .forms import OrderForm
from http import HTTPStatus
from django.test import Client, RequestFactory
from . import views
from .forms import OrderForm


class TransactionTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_main_view(self):
        url = reverse('order_list_url')
        self.assertEqual(resolve(url).func.view_class, views.OrdersListView)

    def test_detail_view(self):
        url = reverse('order_create_url')
        self.assertEqual(resolve(url).func.view_class, views.OrderCreateView)

    def test_view_get(self):
        request = self.factory.get('')
        response = views.OrdersListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_form(self):
        form = OrderForm(
            data={'agent': 'lala', 'comment': 'lolo', 'amount': '456', 'date': '11.05.20'})
        self.assertTrue(form.is_valid())

    def test_form_1(self):
        form = OrderForm(
            data={'agent': '', 'comment': 'lolo', 'amount': '456', 'date': '11.05.20'})
        self.assertFalse(form.is_valid())

    def test_form_2(self):
        form = OrderForm(
            data={'agent': 'lala', 'comment': '', 'amount': '456', 'date': '11.05.20'})
        self.assertFalse(form.is_valid())

    def test_form_3(self):
        form = OrderForm(
            data={'agent': 'lala', 'comment': 'lolo', 'amount': '', 'date': '11.05.20'})
        self.assertFalse(form.is_valid())

    def test_form_4(self):
        form = OrderForm(
            data={'agent': 'lala', 'comment': 'lolo', 'amount': '456', 'date': ''})
        self.assertFalse(form.is_valid())

    def test_form_5(self):
        form = OrderForm(
            data={'agent': 'lala', 'comment': 'lolo', 'amount': '-456', 'date': '11.05.20'})
        self.assertFalse(form.is_valid())

    def test_form_6(self):
        form = OrderForm(
            data={'agent': 'lala', 'comment': 'lolo', 'amount': 'ioio', 'date': '11.05.20'})
        self.assertFalse(form.is_valid())
