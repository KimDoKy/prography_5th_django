from django.test import TestCase, Client
from django.contrib.auth.models import User

class UserCreateTestCase(TestCase):

    def setUp(self):
        self.username = 'tester'
        self.email = 'test@test.com'
        self.password = 'test1234'
        
    def test_create_user(self):
        old_count = User.objects.count()
        u1 = User.objects.create_user(username=self.username,
                                      email=self.email,
                                      password=self.password)
        new_count = User.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_signup(self):
        client = Client()
        res = client.get('/accounts/signup/')
        self.assertEqual(res.status_code, 200)
