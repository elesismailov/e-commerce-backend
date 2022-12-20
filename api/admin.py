from django.contrib import admin

# Register your models here.

from .models import Customer
from .models import Product, Variant, VariantOption, Sku, SkuMapper
from .models import Category
from .models import Brand
from .models import CartItem

from .models import Order, OrderItem, Shipment, StatusCode

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Variant)
admin.site.register(VariantOption)
admin.site.register(Sku)
admin.site.register(SkuMapper)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Shipment)
admin.site.register(StatusCode)

