from django.contrib import admin
from .models import Products, Customer, Order
from .resources import ProductsResource, CustomerResource

from import_export import resources
from .models import Products, Customer

from import_export.admin import ImportExportModelAdmin

class ProductsAdmin(ImportExportModelAdmin):
    resource_class = ProductsResource

class CustomerAdmin(ImportExportModelAdmin):
    resource_class = CustomerResource

# Register your models here.
admin.site.register(Products, ProductsAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order)