from django.db import models
from django import forms


class Country(models.Model):
    COUNTRIES = (
        ('BR', 'Brazil'),
        ('JP', 'Japan'),
        ('PT', 'Portugal'),
        ('US', 'United States'),
    )
    country = models.CharField(max_length=2, choices=COUNTRIES,default='BR')

    def __str__(self):
        return self.country



class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    address= models.CharField(max_length=200)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.ForeignKey(Country)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s' % (self.first_name , self.family_name)


class Product(models.Model):
    description = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer)

    def __str__(self):
        return self.description

class Order(models.Model):
    customer = models.ForeignKey(Customer)
    order_weight = models.IntegerField(max_length=1000)
    price = models.IntegerField(max_length=1000)

    def __str__(self):
            return self.address_line

