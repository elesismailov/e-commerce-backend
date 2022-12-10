from django.test import TestCase, Client

from rest_framework import status

from api.models import Product, Brand, Category

class TestProductViewRoute(TestCase):

    def setUp(self):
        self.c = Client()

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

    def test_structure(self):

        response = self.c.get('/api/products/' + self.product.slug + '/')

        self.assertTrue('name' in response.data)
        self.assertTrue('brand' in response.data)
        self.assertTrue('slug' in response.data)
        self.assertTrue('description' in response.data)
        self.assertTrue('category' in response.data)
        self.assertTrue('in_stock_amount' in response.data)
        self.assertTrue('sold_amount' in response.data)
        self.assertTrue('price' in response.data)
        self.assertTrue('created_at' in response.data)
        self.assertTrue('last_modified' in response.data)

    def test_invalid_slug(self):

        response = self.c.get('/api/products/an-invalid-slug/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)












