# myapp/admin.py
from django.contrib import admin
from .models import UserProfile, Sales

admin.site.register(UserProfile)
admin.site.register(Sales)
