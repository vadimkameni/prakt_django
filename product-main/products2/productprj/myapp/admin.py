from django.contrib import admin
from .models import Orders, Products, Customers

admin.site.register(Products)
admin.site.register(Customers)
admin.site.register(Orders)
