from django.contrib import admin
from .models import UserManager, User, UserProfile

# Register your models here.
# admin.site.register(UserManager)
admin.site.register(User)
admin.site.register(UserProfile)