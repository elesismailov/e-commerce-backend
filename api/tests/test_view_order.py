from django.test import TestCase, Client

from rest_framework import status

from api.models import Customer, Product, Brand, Category, Order, StatusCode, OrderItem

class TestViewOrder(TestCase):

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
        self.i1 = OrderItem.objects.create(
                product = self.product,
                order = self.order,
                price = self.product.id,
                quantity = 1,
                )

    def test_getting_data(self):

        response = self.c.get(
                '/api/orders/' + str(self.order.id) + '/',
                HTTP_AUTHORIZATION='API-KEY ' + self.customer.api_key,
                )

        self.assertTrue('order' in response.data)

        self.assertEqual(
                response.data['order']['id'],
                self.order.id)

        self.assertTrue('order_items' in response.data)


    def test_404_NOT_FOUND(self):

        response = self.c.get(
                '/api/orders/-1234321242/',
                HTTP_AUTHORIZATION='API-KEY ' + self.customer.api_key,
                )

        self.assertEqual(
                response.status_code,
                status.HTTP_404_NOT_FOUND,
                )


