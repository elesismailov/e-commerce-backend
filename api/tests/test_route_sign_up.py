from django.test import TestCase, Client

from rest_framework import status

from api.models import Customer

class TestCustomerSignUp(TestCase):

    def setUp(self):
        self.c = Client()
    

    def test_creating_in_database(self):
        customer_n_before = Customer.objects.count()
        self.assertEqual(customer_n_before, 0)

        response = self.c.post('/api/sign-up/', 
                {
                    "name": "Test Customer",
                    "password": "1234",
                    "email": "testcustomer@gmail.com",
                    "phone": "+123 456 789"
                    },
                content_type='application/json',
                )

        customer_n_after = Customer.objects.count()
        self.assertEqual(customer_n_after, 1)


    def test_201_CREATED(self):
        customer_n_before = Customer.objects.count()
        self.assertEqual(customer_n_before, 0)

        response = self.c.post('/api/sign-up/', 
                {
                    "name": "Test Customer",
                    "password": "1234",
                    "email": "testcustomer@gmail.com",
                    "phone": "+123 456 789"
                    },
                content_type='application/json',
                )

        customer_n_after = Customer.objects.count()
        self.assertEqual(customer_n_after, 1)

        self.assertEqual(
                response.status_code,
                status.HTTP_201_CREATED
                )


    def test_creating_existing_customer(self):

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

        # TEST
        response = self.c.post('/api/sign-up/', 
                {
                    "name": "Test Customer",
                    "password": "1234",
                    "email": "testcustomer@gmail.com",
                    "phone": "+123 456 789"
                    },
                content_type='application/json',
                )

        self.assertEqual(
                response.status_code,
                status.HTTP_409_CONFLICT)



    def test_400_BAD_REQUEST(self):

        response = self.c.post('/api/sign-up/', 
                {
                    #"name": "Test Customer",
                    "password": "1234",
                    "email": "testcustomer@gmail.com",
                    "phone": "+123 456 789"
                    },
                content_type='application/json',
                )
        self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST)

        response = self.c.post('/api/sign-up/', 
                {
                    "name": "Test Customer",
                    #"password": "1234",
                    "email": "testcustomer@gmail.com",
                    "phone": "+123 456 789"
                    },
                content_type='application/json',
                )
        self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST)

        response = self.c.post('/api/sign-up/', 
                {
                    "name": "Test Customer",
                    "password": "1234",
                    #"email": "testcustomer@gmail.com",
                    "phone": "+123 456 789"
                    },
                content_type='application/json',
                )
        self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST)

        response = self.c.post('/api/sign-up/', 
                {
                    "name": "Test Customer",
                    "password": "1234",
                    "email": "testcustomer@gmail.com",
                    #"phone": "+123 456 789"
                    },
                content_type='application/json',
                )
        self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST)

        response = self.c.post('/api/sign-up/', 
                {
                    "name": "Test Customer",
                    #"password": "1234",
                    "email": "testcustomer@gmail.com",
                    #"phone": "+123 456 789"
                    },
                content_type='application/json',
                )
        self.assertEqual(
                response.status_code,
                status.HTTP_400_BAD_REQUEST)









