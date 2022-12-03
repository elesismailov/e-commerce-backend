
from django.test import TestCase

from api.models import Customer

print('hello world')

class TestModelCustomer(TestCase):

    def test_testing(self):

        self.assertEqual(True, True)
