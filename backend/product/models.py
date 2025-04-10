from django.db import models
from category.models import Category
from django.core.validators import MinValueValidator
from basket.models import Basket
STATUS_CHOICES = (
    ("OUT_OF_STOCK", "out of stock"),
    ("NOT_AVAILABLE", "not available"),
    ("IN_STOCK", "in stock")
)


class Product(models.Model):
    id = models.AutoField(primary_key = True )
    name = models.CharField(max_length = 100, blank=False)
    price = models.DecimalField(decimal_places = 2,max_digits = 1000, blank=False)
    status = models.CharField(choices = STATUS_CHOICES, default = "IN_STOCK", max_length=80)
    picture = models.ImageField(blank=False, upload_to='products/')
    category = models.ManyToManyField(Category, related_name="category")
    quantity = models.IntegerField(default=1, editable=False)


    def __str__(self) -> str:
        return f"{self.name} - {self.price}$"
