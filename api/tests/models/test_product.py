from datetime import datetime

from api.tests.test_setup import TestSetup
from api.models import Product


class TestModelProduct(TestSetup):
    def test_create_product(self):
        self.product_data = Product.objects.create(
            name= 'name test models',
            description='description test models',
            price=2.99,
            stock=2,
        )

    def test_booking_data_str(self):
        self.assertEqual(str(self.main_product), "NAME TEST ONE Stock: 1")

    def test_get_product(self):
        product_to_update = Product.objects.get(pk=self.main_product.pk)
        self.assertEqual(product_to_update, self.main_product)

    def test_update_product(self):
        product_to_update = Product.objects.get(pk=self.main_product.pk)
        product_to_update.stock = 2
        product_to_update.save()
        self.assertEqual(product_to_update.stock, 2)

    def test_delete_product(self):
        product_to_update = Product.objects.get(pk=self.main_product.pk)
        product_to_update.delete = True
        product_to_update.save()
        self.assertEqual(product_to_update.delete, True)