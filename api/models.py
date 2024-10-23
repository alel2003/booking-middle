from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    delete = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name.upper()} Stock: {self.stock}"


class Order(models.Model):
    class Status(models.TextChoices):
        NEW = "new"
        IN_PROGRESS = "in_progress"
        DONE = "done"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete = models.BooleanField(default=False)

    @property
    def total_price(self):
        return sum(product.price for product in self.products.all())
