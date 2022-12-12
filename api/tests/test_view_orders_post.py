
from django.test import TestCase, Client

from rest_framework import status

from api.models import Customer, Product, Brand, Category, Order, StatusCode, OrderItem, CartItem

class TestViewOrdersPost(TestCase):

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

        self.cart_item = CartItem.objects.create(
                customer=self.customer,
                product=self.product,
                quantity=2,
                )

    def test_creating_order_items(self):

        quantity = 2

        response = self.c.post(
                '/api/orders/',
                {
                    "cart_items": [
                        {
                            "cart_item_id": self.cart_item.id,
                            "quantity": quantity,
                            },
                        ],
                    },
                HTTP_AUTHORIZATION='API-KEY ' + self.customer.api_key,
                )


        item = OrderItem.objects.get(order=self.order)

        self.assertIsNotNone(item)

        self.assertEqual(item.product.id, self.product.id)

        self.assertEqual(item.quantity, quantity)
        print(response.data)


    def test_400_BAD_REQUEST(self):

        '''Some fields are missing.'''

        quantity = 2

        response = self.c.post(
                '/api/orders/', { "cart_items": [ {
                            "cart_item_id": self.cart_item.id,
                            # "quantity": quantity,
                            }, ], },
                HTTP_AUTHORIZATION='API-KEY ' + self.customer.api_key,
                )


        self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST,
                )


    def test_404_NOT_FOUND(self):

        quantity = 2

        response = self.c.post(
                '/api/orders/', { "cart_items": [ {
                            "cart_item_id": "101200201",
                            "quantity": quantity,
                            }, ], },
                HTTP_AUTHORIZATION='API-KEY ' + self.customer.api_key,
                )


        self.assertEqual(
                response.status_code,
                status.HTTP_404_NOT_FOUND,
                )

    def test_cart_item_becomes_inactive(self):

        quantity = 2

        self.assertTrue(self.cart_item.is_active)

        self.assertIsNone(self.cart_item.checked_out_at)

        response = self.c.post(
                '/api/orders/',
                {
                    "cart_items": [
                        {
                            "cart_item_id": self.cart_item.id,
                            "quantity": quantity,
                            },
                        ],
                    },
                HTTP_AUTHORIZATION='API-KEY ' + self.customer.api_key,
                )

        self.assertFalse(self.cart_item.is_active)

        self.assertIsNotNone(self.cart_item.checked_out_at)
















