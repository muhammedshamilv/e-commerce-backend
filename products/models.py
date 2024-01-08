from django.db import models
from e_commerce.models import AbstractBaseModel

# Create your models here.


class Category(AbstractBaseModel):
    name = models.CharField(max_length=150)


class Product(AbstractBaseModel):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    details = models.TextField()
    availability = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)


class Cart(AbstractBaseModel):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together=["user","product"]

class Order(AbstractBaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    address = models.TextField()
