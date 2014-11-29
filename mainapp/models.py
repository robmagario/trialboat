from django.db import models


class CountryManager(models.Manager):
    def get_by_natural_key(self, initials):
        return self.get(initials=initials)


class Country(models.Model):
    objects = CountryManager()
    initials = models.CharField(max_length=10, default='BR', unique=True)

    def __str__(self):
        return '%s' % self.initials


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
        return '%s %s' % (self.first_name, self.family_name)


class Product(models.Model):
    description = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer)

    def __str__(self):
        return self.description

class Order(models.Model):
    user = models.ForeignKey(Customer)
    address_line = models.CharField(max_length=1000)
    order_weight = models.IntegerField(max_length=1000)
    price = models.IntegerField(max_length=1000)

    def __str__(self):
            return self.address_line

