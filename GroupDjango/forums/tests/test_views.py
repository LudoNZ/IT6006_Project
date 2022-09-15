from django.test import TestCase, Client
from django.urls import reverse
from forums.models import Forum, Comment, Category


# Account Views Test.


class TestListViews(TestCase):

    def setUp(self):
        client = Client()

    def test_project_list_GET(self):
        response = self.client.get(reverse('list_url'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'forums/forum_list.html')
