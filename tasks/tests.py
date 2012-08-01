from django.test import TestCase
from django.core.urlresolvers import reverse

class TasksTest(TestCase):
    def test_login(self):
        response = self.client.post(reverse('userena_signin'), {'username': 'rif', 'password': 'test'})
        self.assertEqual(response.status_code, 200)
         
    def test_incr(self):
        logged_in = self.client.login(username='rif', password='test')
        self.assertTrue(logged_in)
        t1 = Task.objects.all()[0]
        self.assertEqual(t1.priority,2)
        
