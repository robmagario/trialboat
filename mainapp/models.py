from django.db import models

class Product(models.Model):
    description = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)

class Customer(models.Model):
    firstname =models.CharField(max_length=100)
    familyname = models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    zipcode = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


# Create your models here.
