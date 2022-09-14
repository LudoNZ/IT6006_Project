from django.test import TestCase
from forums.models import Category, Forum


# Models tests
class TestModel(TestCase):
    def create_should_create_category(self):
        cat = Category.objects.create_category(name='C#', position='5')
        cat.save()
        self.assertEqual(new_cat.__str__(), new_cat.name)
