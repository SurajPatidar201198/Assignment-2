from django.db import models

# Create your models here.

class Product(models.Model):
    column_name_1 = models.CharField(max_length=50)
    column_name_2 = models.CharField(max_length=50)

class ProductLink(models.Model):
    link = models.CharField(max_length=500)
    