from django.test import TestCase, Client

from rest_framework import status

from api.models import Customer

class TestCustomerLogIn(TestCase):

    def setUp(self):
        self.c = Client()

        # create 'existing' user
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

    def test_getting_api_key(self):
        response = self.c.post('/api/log-in/', 
                {
                    "email": "testcustomer@gmail.com",
                    "password": "1234",
                    },
                content_type='application/json',
                )

        self.assertTrue(hasattr(response.data, 'api_key'))

        self.assertEqual(
                response.data.get('api_key'),
                self.customer.api_key
                )
    

    def test_404_NOT_FOUND(self):
        response = self.c.post('/api/log-in/', 
                {
                    "email": "someemailthatdoesntexist@gmail.com",
                    "password": "1234",
                    },
                content_type='application/json',
                )

        self.assertEqual(
                response.status_code,
                status.HTTP_404_NOT_FOUND,
                )


    def test_400_BAD_REQUEST(self):
        response = self.c.post('/api/log-in/', 
                {
                    "email": "testcustomer@gmail.com",
                    "password": "wrong-password",
                    },
                content_type='application/json',
                )

        self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST,
                )

    def test_getting_customer_data(self):

        response = self.c.post('/api/log-in/', 
                {
                    "email": "testcustomer@gmail.com",
                    "password": "1234",
                    },
                content_type='application/json',
                )


        self.assertTrue(hasattr(response.data, 'api_key'))
        self.assertTrue(hasattr(response.data, 'customer_data'))

        # test count of fields
        # test compare some fields







