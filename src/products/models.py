from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)  # max_lentgth is required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=65, decimal_places=2)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField()  # null=True, default=True
