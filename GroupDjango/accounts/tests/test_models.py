from django.test import TestCase
from django.contrib.auth import get_user_model, login as auth_login
from django.urls import reverse

# Account Model Test.


class TestAccountModel(TestCase):
    # Test setup
    def setUp(self):
        self.signup_url = reverse('signup')
        self.user = {
            'username': 'test',
            'password': '12test12',
            'password2': '12test12',
            'age': 10,
        }
        return super().setUp()

    def test_signup_user(self):
        response = self.client.post(
            self.signup_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 200)
        # not 302 because using a redirect to send back the homepage view?

    # Test autentication
    # def test_user_authenticated(self):
    #     user = get_user_model().objects.create_user(
    #         username='test', password='12test12')
    #     login = auth_login(request, user)
    #     self.assertTrue((self.user is not None) and self.user.is_authenticated)
    #     self.assertEqual(self.user, 'test')
