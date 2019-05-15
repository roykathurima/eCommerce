from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    featured = models.BooleanField(default=False)