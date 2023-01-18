from django.db import models

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=256, null=False)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    product_category = models.CharField(max_length=256, null=False)
    product_image = models.ImageField(upload_to="products", null=True, blank=True)

class HomePageProducts(models.Model):
    product_name = models.CharField(max_length=256, null=False)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    product_category = models.CharField(max_length=256, null=False)
    product_image = models.ImageField(upload_to="products", null=True, blank=True)