from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    address= models.CharField(max_length=200)
    zip = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)

    def __str__(self):
        return '%s %s' % (self.firstname,self.familyname)


class Product(models.Model):
    description = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer)

    def __str__(self):
        return self.description