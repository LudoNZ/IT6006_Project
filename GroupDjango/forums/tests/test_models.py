from django.test import TestCase
from forums.models import Forum, Comment, Category
from django.utils import timezone
from django.contrib.auth import get_user_model


# Forum model Test.

class TestModelForums(TestCase):

    # Test setup
    @classmethod
    def setUp(cls):
        cls.test_user = get_user_model().objects.create_user(
            username='test', password='12test12')
        cls.test_category = Category.objects.create(name="PHP", position=0)
        cls.test_forum = Forum.objects.create(title="Python question", slug="python-question", category=cls.test_category,
                                              description="bra bra", user=cls.test_user)
        cls.test_comment = Comment.objects.create(
            user=cls.test_user, forum=cls.test_forum, message="I have no idea.")

    def test_create_category(self):
        self.assertEqual(str(self.test_category.name), "PHP")

    def test_create_forum(self):
        self.assertEqual(str(self.test_forum.title), "Python question")

    def test_create_comment(self):
        self.assertEqual(str(self.test_comment.message), "I have no idea.")
