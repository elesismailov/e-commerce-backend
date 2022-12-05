from django.contrib import admin

# Register your models here.

from .models import Customer
from .models import Product
from .models import Category
from .models import Brand

# class CustomerAdmin(admin):
#     model = Customer
#     list_display = ['email', 'name']
# 
# admin.site.register(Customer, CustomerAdmin)

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
