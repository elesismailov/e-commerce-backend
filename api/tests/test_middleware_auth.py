from django.test import TestCase, Client

from rest_framework import status

from api.models import Customer

class TestAuthenticationMiddleware(TestCase):

    def setUp(self):
        self.c = Client()

        customer_n_before = Customer.objects.count()
        self.assertEqual(customer_n_before, 0)
        customer = Customer.objects.create(
                name  = 'Test Customer',
                phone = '+123 456 789',
                email = 'testcustomer@gmail.com',
                password = '1234',
                )
        customer_n_after = Customer.objects.count()
        self.assertEqual(customer_n_after, 1)

        self.customer = customer

    def test_letting_through(self):
        with self.modify_settings(
                API_PROTECTED_ROUTES={
                    'append': [
                        '/api/products/',
                        ],
                    }
                ):
            response = self.c.get(
                    '/api/products/',
                    HTTP_AUTHORIZATION='API-KEY ' + self.customer.api_key,
                    )

            self.assertEqual(
                    response.status_code,
                    status.HTTP_200_OK,
                    )
            self.assertTrue('count' in response.data)

    def test_401_UNAUTHORIZED(self):

        with self.modify_settings(
                API_PROTECTED_ROUTES={
                    'append': [
                        '/api/products/',
                        ],
                    }
                ):
            response = self.c.get(
                    '/api/products/',
                    HTTP_AUTHORIZATION='API-KEY wrongApiKey',
                    )

            self.assertEqual(
                    response.status_code,
                    status.HTTP_401_UNAUTHORIZED
                    )










