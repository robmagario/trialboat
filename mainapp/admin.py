from django.contrib import admin
from mainapp.models import Product
from mainapp.models import Customer
from mainapp.models import Order
from mainapp.models import Country


class ProductAdmin(admin.ModelAdmin):
    list_display = ('description', 'customer')


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Country)
# Register your models here.
