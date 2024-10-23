from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import Product, Order


class TestAPI(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuserapi", password="password"
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"JWT {str(refresh.access_token)}")
        
        self.main_product = Product.objects.create(
            name= 'name api test',
            description='description api test',
            price=5.99,
            stock=2,
        )

        self.json_create_product = {
            "name": "json name",
            "description": "json description",
            "price": 6.99,
            "stock" : 3
        }

        self.json_update_product = {
            "stock": 4
        }

        self.json_delete_product = {
            "delete": True
        }

        self.main_order = Order.objects.create(
            user=self.user
        )

        self.main_order.products.add(self.main_product.id)

        self.json_create_order = {
            "products": [{"id": 1}],
        }

        self.json_update_order = {
            "status": "done"
        }

        self.json_delete_order = {
            "delete": True
        }