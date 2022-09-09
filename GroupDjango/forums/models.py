from django.contrib.auth import get_user_model
from django import template
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings


User = get_user_model()
register = template.Library()


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name


class Forum(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    category = models.ForeignKey(
        Category, related_name="categories", on_delete=models.CASCADE)
    description = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    is_closed = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='forums',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("forums:single", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["title"]


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='Comments',
                             on_delete=models.CASCADE)
    forum = models.ForeignKey(
        Forum, related_name='comments', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    message = models.TextField()

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("forums:single", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['created_at']
