from django.test import TestCase

from api.models import Customer

class TestModelCustomer(TestCase):
    

    def test_customer_creation(self):
        
        customer_n_before = Customer.objects.count()

        self.assertEqual(customer_n_before, 0)

        customer = Customer.objects.create(
                name  = 'Customer Name',
                phone = '+123 456 789 10',
                email = 'customer@gmail.com',
                password = '1234',
                )

        customer_n_after = Customer.objects.count()

        self.assertEqual(customer_n_after, 1)


    def test_has_api_key(self):

        # create user
        customer_n_before = Customer.objects.count()
        self.assertEqual(customer_n_before, 0)
        customer = Customer.objects.create(
                name  = 'Customer Name',
                phone = '+123 456 789 10',
                email = 'customer@gmail.com',
                password = '1234',
                )
        customer_n_after = Customer.objects.count()
        self.assertEqual(customer_n_after, 1)

        #test
        self.assertTrue(hasattr(customer, 'api_key'))


    def test_changing_api_key_on_update(self):

        # create user
        customer_n_before = Customer.objects.count()
        self.assertEqual(customer_n_before, 0)
        customer = Customer.objects.create(
                name  = 'Customer Name',
                phone = '+123 456 789 10',
                email = 'customer@gmail.com',
                password = '1234',
                )
        customer_n_after = Customer.objects.count()
        self.assertEqual(customer_n_after, 1)

        self.assertTrue(hasattr(customer, 'api_key'))

        #test
        old_api_key = customer.api_key

        customer.name = 'New Name'
        customer.save()

        new_api_key = customer.api_key

        self.assertNotEqual(old_api_key, new_api_key)


    def test_customer_deletion(self):
        # create user
        customer_n_before = Customer.objects.count()
        self.assertEqual(customer_n_before, 0)
        customer = Customer.objects.create(
                name  = 'Customer Name',
                phone = '+123 456 789 10',
                email = 'customer@gmail.com',
                password = '1234',
                )
        customer_n_after = Customer.objects.count()
        self.assertEqual(customer_n_after, 1)

        customer.delete()

        #test
        customer_n_after = Customer.objects.count()
        self.assertEqual(customer_n_after, 0)














