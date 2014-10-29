from django.db import models

class Product(models.Model):
    description = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)



# Create your models here.
