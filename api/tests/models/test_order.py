from datetime import datetime

from api.tests.test_setup import TestSetup
from api.models import Order


class TestModelProduct(TestSetup):
    def test_create_order(self):
        self.order_data = Order.objects.create(
            user=self.user,
            created_at=datetime.now()
        )
        
        self.main_order.products.add(self.main_product.id)
        self.assertEqual(self.main_order.products.count(), 1)
        self.assertEqual(self.main_order.products.first(), self.main_product)


    def test_get_order(self):
        order_to_update = Order.objects.get(pk=self.main_order.pk)
        self.assertEqual(order_to_update, self.main_order)

    def test_update_order(self):
        order_to_update = Order.objects.get(pk=self.main_order.pk)
        order_to_update.status = "in_progress"
        order_to_update.save()
        self.assertEqual(order_to_update.status, "in_progress")

    def test_delete_order(self):
        order_to_update = Order.objects.get(pk=self.main_order.pk)
        order_to_update.delete = True
        order_to_update.save()
        self.assertEqual(order_to_update.delete, True)