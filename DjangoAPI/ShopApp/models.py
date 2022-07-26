from django.db import models

# Create your models here.

class Products(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=1000)
    ProductBrand = models.CharField(max_length=100)
