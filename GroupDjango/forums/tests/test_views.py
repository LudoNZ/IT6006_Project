from django.test import TestCase, Client
from django.urls import reverse
from forums.models import Forum, Comment, Category


# Account Views Test.


class TestViews(TestCase):

    def setUp(self):
        client = Client()
        self.list_url = reverse('ListForums')

    def test_project_list_GET(self):
        response = self.client.get(reverse('list_url'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'forums/forum_list.html')
