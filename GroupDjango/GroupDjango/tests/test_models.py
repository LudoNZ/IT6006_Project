from django.test import TestCase
from django.contrib.auth import get_user_model
from forums.models import Category, Forum

User = get_user_model()


# Tests User Model
class TestModelUser(TestCase):

    def test_should_create_user(self):
        user = User.objects.create_user(
            username='testuser', email='email@app.com')
        user.set_password('password12!')
        user.save()
        self.assertEqual(str(user), 'testuser')


# Tests Forum App Models
class TestModelCategory(TestCase):

    def create_should_create_category(self):
        cat = Category(name='C#', position='')
        cat.save()
        self.assertEqual(str(cat), 'c#')


class TestModelForum(TestCase):

    def test_should_create_forum(self):
        user = User.objects.create_user(
            username='testuser', email='email@app.com')
        user.set_password('password12!')
        user.save()

        forum = Forum(title='Can I ask a question for Python?', category='Python',
                      description='I do not know about Pytest!', is_closed=Flase, user=user)

        forum.save()
        self.assertEqual(str(forum), 'Can I ask a question for Python?')
