from django.contrib import admin

# Register your models here.

from .models import Customer

# class CustomerAdmin(admin):
#     model = Customer
#     list_display = ['email', 'name']
# 
# admin.site.register(Customer, CustomerAdmin)

admin.site.register(Customer)
