from django.test import TestCase, Client

from rest_framework import status

from api.models import Customer, Product, Brand, Category, CartItem

class TestViewCartPost(TestCase):

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

    def test_getting_data(self):

        quantity = 2

        response = self.c.post(
                '/api/cart/',
                {
                    "product_id": self.product.id,
                    "quantity": quantity,
                    },
                HTTP_AUTHORIZATION='API-KEY ' + self.customer.api_key,
                )

        # print(response.data)

        item = CartItem.objects.get(customer=self.customer)

        self.assertIsNotNone(item)

        self.assertEqual(item.product.id, self.product.id)

        self.assertEqual(item.quantity, quantity)


    def test_400_BAD_REQUEST(self):

        response = self.c.post(
                '/api/cart/',
                {
                    "product_id": self.product.id,
                    # "quantity": 1,
                    },
                HTTP_AUTHORIZATION='API-KEY ' + self.customer.api_key,
                )

        # print(response.data)

        self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST
                )


    def test_404_NOT_FOUND_product(self):

        response = self.c.post(
                '/api/cart/',
                {
                    "product_id": 123451234, # WRONG ID
                    "quantity": 1,
                    },
                HTTP_AUTHORIZATION='API-KEY ' + self.customer.api_key,
                )

        # print(response.data)

        self.assertEqual(
                response.status_code,
                status.HTTP_404_NOT_FOUND,
                )





