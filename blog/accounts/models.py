from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
# from django.db import models
# from account.conf import settings


# class UserBio(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="accounts", on_delete=models.CASCADE)
#     birth_date = models.DateField(null=True, blank=True)
#     country = models.CharField(max_length=30, blank=True)
#     city = models.CharField(max_length=30, blank=True)