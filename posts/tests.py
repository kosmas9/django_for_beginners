from django.test import TestCase #reate a sample database
from .models import Post

class TestPostModel(TestCase):
    def setUp(self):
        Post.objects.create(text='just a text')
    def test_text_context(self):
        post=Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name,'just a text')
