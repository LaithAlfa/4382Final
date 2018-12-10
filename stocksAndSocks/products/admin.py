from django.contrib import admin

from .models import Product, Buyer, Payment

admin.site.register(Product)

admin.site.register(Buyer)

admin.site.register(Payment)
