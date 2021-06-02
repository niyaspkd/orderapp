from import_export import resources
from .models import Products, Customer

class ProductsResource(resources.ModelResource):
    class Meta:
        model = Products

class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer