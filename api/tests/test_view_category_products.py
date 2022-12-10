from django.test import TestCase, Client

from rest_framework import status

from api.models import Product, Brand, Category

class TestCategoryProducts(TestCase):

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


    def test_getting_data(self):

        response = self.c.get('/api/categories/' + self.category.slug + '/products/')

        self.assertTrue('results' in response.data)
        self.assertEqual(response.data['results'][0]['name'], self.product.name)


    def test_invalid_slug(self):

        response = self.c.get('/api/categories/an-invalid-slug/products/')

        self.assertEqual(
                response.status_code,
                status.HTTP_404_NOT_FOUND,
                )









