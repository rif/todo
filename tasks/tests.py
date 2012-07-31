from .api import API
from adrest.tests.utils import AdrestTestCase

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)



class SimpleTestCase(AdrestTestCase):
    api = API

    def test_base(self):
        uri = self.reverse('task')
        self.assertEqual(uri, '/simple/task/')
        response = self.get_resource('task')
        self.assertContains(response, 'true')