# admin.py en tu aplicación de usuarios

from django.contrib import admin
from .models import UserItem

admin.site.register(UserItem)
