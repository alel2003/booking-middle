from django.urls import path
from .views import (
    ListProducts,
    CreateProduct,
    ProductDetails,
    UpdateProductDetails,
    DeleteProductDetails,
    ListOrders,
    CreateOrder,
    OrderDetails,
    UpdateOrderDetails,
    DeleteOrderDetails,
)


urlpatterns = [
    path("products/", ListProducts.as_view(), name="products-list"),
    path("create-product/", CreateProduct.as_view(), name="create-product"),
    path("get-product-details/<int:pk>/", ProductDetails.as_view(), name="get-product-details"),
    path(
        "update-product-details/<int:pk>/",
        UpdateProductDetails.as_view(),
        name="update-product-details",
    ),
    path(
        "delete-product-details/<int:pk>/",
        DeleteProductDetails.as_view(),
        name="delete-product-details",
    ),
    path("orders/", ListOrders.as_view(), name="orders-list"),
    path("create-order/", CreateOrder.as_view(), name="create-order"),
    path("get-order-details/<int:pk>/", OrderDetails.as_view(), name="get-order-details"),
    path(
        "update-order-details/<int:pk>/",
        UpdateOrderDetails.as_view(),
        name="update-order-details",
    ),
    path(
        "delete-order-details/<int:pk>/",
        DeleteOrderDetails.as_view(),
        name="delete-order-details",
    ),
]
