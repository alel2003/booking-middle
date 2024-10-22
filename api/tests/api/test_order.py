from django.urls import reverse
from rest_framework import status
from api.tests.api.test_api import TestAPI


class TestApiOrder(TestAPI):
    def test_get_orders(self):
        url = reverse('orders-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_get_order_details(self):
        url = reverse('get-order-details', args=[self.main_order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_order(self):
        url = reverse('create-order')
        response = self.client.post(url, self.json_create_order, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["products"], self.json_create_order["products"])

    def test_update_order(self):
        url = reverse('update-order-details', args=[self.main_order.id])
        response = self.client.patch(url, self.json_update_order, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["status"], self.json_update_order["status"])

    def test_delete_order(self):
        url = reverse('delete-order-details', args=[self.main_order.id])
        response = self.client.patch(url, self.json_delete_order, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["delete"], self.json_delete_order["delete"])
        