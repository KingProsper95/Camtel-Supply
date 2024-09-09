from django.db import models
from .validators import validate_cameroonian_phone_number
from django.core.validators import MinValueValidator

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=255,
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True)
    number = models.CharField(
        unique= True,
        max_length= 13,
        validators= [validate_cameroonian_phone_number]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Entity(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.PROTECT, default=1)
    status = models.CharField(max_length=255)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, default=1)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, default=1)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)