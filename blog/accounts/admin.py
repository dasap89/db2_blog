from django.contrib import admin
# from .models import UserBio
from django.contrib.auth import get_user_model

User = get_user_model()

# Register your models here.

# admin.site.unregister(User)
admin.site.register(User)
# admin.site.register(UserBio)
