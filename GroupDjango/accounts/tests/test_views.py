from django.test import TestCase
from django.urls import reverse

# Account Views Test.


class TestSignupViews(TestCase):

    def test_should_show_signin_page(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")


class TestLoginViews(TestCase):

    def test_should_show_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
