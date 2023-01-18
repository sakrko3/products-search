from django.db import models
from django.utils import timezone


class Product(models.Model):
    region=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    product=models.CharField(max_length=255)
    quantity=models.IntegerField()
    unit_price=models.FloatField()
    order_date=models.DateField(default=timezone.now)


    def __str__(self):
            return self.product  