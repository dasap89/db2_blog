from __future__ import unicode_literals

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(
        max_length=60,
        null=False,
        blank=False)
    body = models.TextField(
        null=True,
        blank=False)
    image = models.ImageField(
        upload_to='post_images/',
        default='post_images/does_not_exist_picture.jpg',
        null=True,
        blank=True)
    author = models.ForeignKey(
        User,
        related_name='author',
        null=False,
        blank=False)

    def __str__(self):
        return '{}'.format(self.title)