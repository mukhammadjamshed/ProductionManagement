from django.contrib import admin

from django.contrib import admin
from .models import Product, RawMaterial, ProductMaterial, Warehouse, WarehouseQuantity

admin.site.register(Product)
admin.site.register(RawMaterial)
admin.site.register(ProductMaterial)
admin.site.register(Warehouse)
admin.site.register(WarehouseQuantity)
