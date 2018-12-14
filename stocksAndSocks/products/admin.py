from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from .models import Product, Buyer, Payment

admin.site.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Buyer)

admin.site.register(Payment)
