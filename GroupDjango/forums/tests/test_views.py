from django.test import TestCase, Client
from django.urls import reverse
from forums.models import Forum, Comment, Category
from django.contrib.auth import get_user_model

# Forum Views Test.
client = Client()


class TestForumListViews(TestCase):

    def test_forum_list_view(self):
        response = client.get(reverse('forums:all'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'forums/forum_list.html')


class TestForumUnsolvedListView(TestCase):

    def test_forum_unsolved_list_view(self):
        response = client.get(reverse('forums:selected_unsolved'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'forums/forum_list_selected_unsolve.html')


class TestForumDetailView(TestCase):

    @classmethod
    def setUp(cls):
        cls.test_user = get_user_model().objects.create_user(
            username='test', password='12test12')
        cls.test_category = Category.objects.create(name="PHP", position=0)
        cls.test_forum = Forum.objects.create(title="Python question", slug="python-question", category=cls.test_category,
                                              description="bla bla bla", user=cls.test_user)
        cls.test_comment = Comment.objects.create(
            user=cls.test_user, forum=cls.test_forum, message="I have no idea.")

    def test_forum_detail_view(self):

        response = client.get(
            reverse('forums:single', args=[self.test_forum.pk]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'forums/forum_detail.html')
