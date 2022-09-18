from django.test import TestCase
from django.contrib.auth import get_user_model


# # Account Model Test.
# class TestAccountModel(TestCase):
#     # Test setup
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username='test', password='12test12')
#         self.user.save()

#     def tearDown(self):
#         self.user.delete()

#     # Test autentication
#     def test_user_authenticated(self):
#         login = self.client.login(username='test', password='12test12')
#         self.assertTrue((self.user is not None) and self.user.is_authenticated)
#         self.assertEqual(self.user, 'test')
