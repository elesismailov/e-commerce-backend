from django.contrib import admin

# Register your models here.

from .models import Customer
from .models import Product
from .models import Category
from .models import Brand
from .models import Cart, CartItem

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Cart)
admin.site.register(CartItem)
