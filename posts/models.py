from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField()

#when a post is created, take the first 50 characters of the text field as the name of the post
    def __str__(self):
        return self.text[:50]