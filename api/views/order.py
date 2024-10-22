from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from api.serializers import OrderSerializers, OrderCreateSerializers
from api.models import Order
from api.cache import Caching


class AuthRequiredMixin:
    permission_classes = [IsAuthenticated]


class BaseOrderData:
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

class CacheBase:
    def get_queryset(self):
        return Caching.get_base_model(key='order', obj=Order)


class ListOrders(BaseOrderData, CacheBase, generics.ListAPIView):
    # adding cache by user
    def get_orders(self):
        user_id = self.request.user.id
        cache_order_for_user = Caching.cache_orders_for_user(user_id=user_id)
        return cache_order_for_user
        


class CreateOrder(AuthRequiredMixin, generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderDetails(BaseOrderData, CacheBase, AuthRequiredMixin, generics.RetrieveAPIView):
    # adding cache by user
    def get_orders(self):
        user_id = self.request.user.id
        cache_order_for_user = Caching.cache_orders_for_user(user_id=user_id)
        return cache_order_for_user


class UpdateOrderDetails(BaseOrderData, AuthRequiredMixin, generics.UpdateAPIView):
    pass


class DeleteOrderDetails(BaseOrderData, AuthRequiredMixin, generics.UpdateAPIView):
    pass
