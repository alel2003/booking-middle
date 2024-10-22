from django.urls import reverse
from rest_framework import status
from api.tests.api.test_api import TestAPI


class TestApiProduct(TestAPI):
    def test_get_products(self):
        url = reverse('products-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_get_product_details(self):
        url = reverse('get-product-details', args=[self.main_product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        url = reverse('create-product')
        response = self.client.post(url, self.json_create_product, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["name"], self.json_create_product["name"])

    def test_update_product(self):
        url = reverse('update-product-details', args=[self.main_product.id])
        response = self.client.patch(url, self.json_update_product, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["stock"], self.json_update_product["stock"])

    def test_delete_product(self):
        url = reverse('delete-product-details', args=[self.main_product.id])
        response = self.client.patch(url, self.json_delete_product, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["delete"], self.json_delete_product["delete"])
        