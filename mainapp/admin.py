from django.contrib import admin
from mainapp.models import Product
from mainapp.models import Customer
from mainapp.models import Order

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
# Register your models here.
