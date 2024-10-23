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


class CacheOrderUser:
    def get_orders(self):
        """adding cache by user"""
        user_id = self.request.user.id
        cache_order_for_user = Caching.cache_orders_for_user(user_id=user_id)
        return cache_order_for_user


class ListOrders(BaseOrderData, CacheOrderUser, generics.ListAPIView):
    def get_queryset(self):
        """cache orders"""
        return Caching.get_base_model(key='orders', obj=Order)


class CreateOrder(BaseOrderData, AuthRequiredMixin, generics.CreateAPIView):
    serializer_class = OrderCreateSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderDetails(BaseOrderData, CacheOrderUser, AuthRequiredMixin, generics.RetrieveAPIView):
     def get_queryset(self):
        order_id = self.kwargs.get('pk')
        return Caching.cache_get_details(key='order', obj=Order, model_id=order_id)


class UpdateOrderDetails(BaseOrderData, AuthRequiredMixin, generics.UpdateAPIView):
    pass


class DeleteOrderDetails(BaseOrderData, AuthRequiredMixin, generics.UpdateAPIView):
    pass
