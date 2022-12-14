from django.test import TestCase, Client

from rest_framework import status
import json

from api.models import Customer, Product, Brand, Category, Order, StatusCode

class TestViewProducts(TestCase):

    def setUp(self):
        self.c = Client()

        self.customer = Customer.objects.create(
                name  = 'Customer Name',
                phone = '+123 456 789 10',
                email = 'customer@gmail.com',
                password = '1234',
                )
        
        self.category = Category.objects.create(
                name  = 'Parent',
                description = 'This is the parent category.',
                )

        self.brand = Brand.objects.create(
                name  = 'Poma',
                description = 'This is the parent category.',
                )

#         self.product = Product.objects.create(
#                 name = 'Test Product 1',
#                 description = 'This is the description of the product.',
#                 category = self.category,
#                 brand = self.brand,
#                 in_stock_amount = 12,
#                 sold_amount = 12,
#                 price = 1234,
#                 )
#         self.status_code = StatusCode.objects.create(
#                 code = 0,
#                 name = 'Awaiting',
#                 description = "When order has not been procced yet."
#                 )
# 
#         self.order = Order.objects.create(
#                 customer = self.customer,
#                 customer_comment = "This should be good.",
#                 status_code = self.status_code,
#                 )
# 
    def test_creating_product(self):

        count = Product.objects.count()

        response = self.c.post('/admin/products/',
                json.dumps({
                    'name': 'Test Product 1',
                    'description': 'This is the legendary test product.',
                    'category_id': self.category.id,
                    'brand_id': self.brand.id,
                    'in_stock_amount': 10,
                    'sold_amount': 0,
                    'price': 123,
                    }),
                content_type='application/json',
                )

        self.assertEqual(Product.objects.count(), count + 1)


    def test_400_missing_fields(self):
        response = self.c.post('/admin/products/',
                json.dumps({
                    'name': 'Test Product 1',
                    'description': 'This is the legendary test product.',
                    'category_id': self.category.id,
                    'brand_id': self.brand.id,
                    'in_stock_amount': 10,
                    'sold_amount': 0,
                    #'price': 123,
                    }),
                content_type='application/json',
                )
        self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST,
                )

        response = self.c.post('/admin/products/',
                json.dumps({
                    'name': 'Test Product 1',
                    'description': 'This is the legendary test product.',
                    'category_id': self.category.id,
                    # 'brand_id': self.brand.id,
                    'in_stock_amount': 10,
                    'sold_amount': 0,
                    'price': 123,
                    }),
                content_type='application/json',
                )
        self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST,
                )

        response = self.c.post('/admin/products/',
                json.dumps({
                    'name': 'Test Product 1',
                    # 'description': 'This is the legendary test product.',
                    'category_id': self.category.id,
                    'brand_id': self.brand.id,
                    'in_stock_amount': 10,
                    'sold_amount': 0,
                    'price': 123,
                    }),
                content_type='application/json',
                )
        self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST,
                )

        response = self.c.post('/admin/products/',
                json.dumps({
                    # 'name': 'Test Product 1',
                    'description': 'This is the legendary test product.',
                    'category_id': self.category.id,
                    'brand_id': self.brand.id,
                    'in_stock_amount': 10,
                    'sold_amount': 0,
                    'price': 123,
                    }),
                content_type='application/json',
                )
        self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST,
                )


    def test_getting_product(self):
        
        response = self.c.post('/admin/products/',
                json.dumps({
                    # 'name': 'Test Product 1',
                    'description': 'This is the legendary test product.',
                    'category_id': self.category.id,
                    'brand_id': self.brand.id,
                    'in_stock_amount': 10,
                    'sold_amount': 0,
                    'price': 123,
                    }),
                content_type='application/json',
                )

        self.assertTrue('product' in response.data)
        self.assertTrue('id' in response.data.get('product'))









