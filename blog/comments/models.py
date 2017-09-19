from __future__ import unicode_literals

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Comment(models.Model):
    post = models.ForeignKey('posts.Post', related_name='comments')
    comment_author = models.ForeignKey(
        User,
        related_name='comment_author',
        null=False,
        blank=False)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
