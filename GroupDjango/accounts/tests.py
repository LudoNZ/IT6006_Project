from django.test import TestCase
from django.urls import reverse

# Account Views Test.


class TestViews(TestCase):
    def test_should_show_register_page(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_shold_show_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")

    def test_should_signup_user(self):
        self.user = {
            "username": "username",
            "age": 10,
            "password": "password",
            "password2": "password",
        }

        response = self.client.post(reverse("signup"), self.user)
        self.assertEqual(response.status_code, 200)
