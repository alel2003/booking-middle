from rest_framework import serializers
from .models import Product, Order


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "status", "products", "created_at", "delete", "updated_at"]


class ProductCreateSerializers(serializers.Serializer):
    id = serializers.IntegerField()


class OrderCreateSerializers(serializers.Serializer):
    # creating an order, and adding the object id to the products field
    products = ProductCreateSerializers(many=True)
    def create(self, validated_data,):
        user = self.context['request'].user
        order = Order.objects.create(user=user)
        
        products = validated_data.pop('products')
        for product in products:
            product_obj = Product.objects.get(id=product['id'])
            order.products.add(product_obj)
        
        return order

