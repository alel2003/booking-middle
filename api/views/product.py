from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from api.serializers import ProductSerializers
from api.models import Product
from api.cache import Caching

class AuthRequiredMixin:
    permission_classes = [IsAuthenticated]


class BaseProductData:
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class CacheBase:
    def get_queryset(self):
        return Caching.get_base_model(key='product', obj=Product)
    


class ListProducts(BaseProductData, CacheBase, generics.ListAPIView):
    pass


class CreateProduct(BaseProductData, AuthRequiredMixin, generics.CreateAPIView):
    pass


class ProductDetails(BaseProductData, AuthRequiredMixin, CacheBase, generics.RetrieveAPIView):
    pass


class UpdateProductDetails(BaseProductData, AuthRequiredMixin, generics.UpdateAPIView):
    pass


class DeleteProductDetails(BaseProductData, AuthRequiredMixin, generics.UpdateAPIView):
    pass
