from django.contrib import admin

# Register your models here.

from .models import Customer
from .models import Product
from .models import Category
from .models import Brand
from .models import CartItem

from .models import Order, OrderItem, Shipment, StatusCode

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Shipment)
admin.site.register(StatusCode)

