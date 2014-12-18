from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail

class CountryManager(models.Manager):
    def get_by_natural_key(self, initials):
        return self.get(initials=initials)


class Country(models.Model):
    objects = CountryManager()
    initials = models.CharField(max_length=10, default='BR', unique=True)

    def __str__(self):
        return '%s' % self.initials


class Customer(models.Model):
    user = models.ForeignKey(User)
    address= models.CharField(max_length=200)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.ForeignKey(Country)


    def __str__(self):
        return '%s' % self.user


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


@receiver(post_save, sender=Product)
def product_registered(created, instance, **kwargs):
    if created:
        email = """Hello %s!

We would like to inform you that your product '%s' has arrived. Please login to %s to pay for your product so that we forward your product to you.

Sincerely,
%s
        """ % (instance.customer.user.first_name, instance.description, "http://127.0.0.1:8080", "Trial Boat")
        send_mail("Your product has arrived!", email, "admin@magario.com", [instance.customer.user.email],
                  fail_silently=False)