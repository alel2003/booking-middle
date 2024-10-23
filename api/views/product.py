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
    


class ListProducts(BaseProductData, generics.ListAPIView):
    def get_queryset(self):
        return Caching.get_base_model(key='products', obj=Product)


class CreateProduct(BaseProductData, AuthRequiredMixin, generics.CreateAPIView):
    pass


class ProductDetails(BaseProductData, AuthRequiredMixin, generics.RetrieveAPIView):
    def get_queryset(self):
        product_id = self.kwargs.get('pk')
        return Caching.cache_get_details(key='product', obj=Product, model_id=product_id)


class UpdateProductDetails(BaseProductData, AuthRequiredMixin, generics.UpdateAPIView):
    pass


class DeleteProductDetails(BaseProductData, AuthRequiredMixin, generics.UpdateAPIView):
    pass
