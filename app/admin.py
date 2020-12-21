from django.contrib import admin

# Register your models here.

from .models import Customer, Product, Order, Profesional

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profesional)


