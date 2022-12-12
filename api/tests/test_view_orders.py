from django.test import TestCase, Client

from rest_framework import status

from api.models import Customer, Product, Brand, Category, Order, StatusCode

class TestViewCart(TestCase):

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

        self.product = Product.objects.create(
                name = 'Test Product 1',
                description = 'This is the description of the product.',
                category = self.category,
                brand = self.brand,
                in_stock_amount = 12,
                sold_amount = 12,
                price = 1234,
                )
        self.status_code = StatusCode.objects.create(
                code = 0,
                name = 'Awaiting',
                description = "When order has not been procced yet."
                )

        self.order = Order.objects.create(
                customer = self.customer,
                customer_comment = "This should be good.",
                status_code = self.status_code,
                )

    def test_getting_data(self):


        response = self.c.get(
                '/api/orders/',
                HTTP_AUTHORIZATION='API-KEY ' + self.customer.api_key,
                )

        # print(response.data)

        self.assertTrue('orders' in response.data)

        self.assertEqual(
                response.data['orders'][0]['customer_comment'], 
                self.order.customer_comment)






