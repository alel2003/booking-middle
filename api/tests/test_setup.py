from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from datetime import datetime


from api.models import Product, Order


class TestSetup(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password")

        self.main_product = Product.objects.create(
            name= 'name test one',
            description='description test one',
            price=1.99,
            stock=1,
        )

        self.main_order = Order.objects.create(
            user=self.user,
            created_at=datetime.now()
        )

        self.main_order.products.add(self.main_product.id)
