from django.test import TestCase
from django.core.urlresolvers import reverse
from tasks.models import Task

class TasksTest(TestCase):
    def test_login(self):
        response = self.client.post(reverse('userena_signin'), {'username': 'rif', 'password': 'test'})
        self.assertEqual(response.status_code, 200)
         
    def test_incr(self):
        self.client.login(username='rif', password='test')        
        
