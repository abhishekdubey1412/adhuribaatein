from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'description','password', 'image')

admin.site.register(UserProfile, UserProfileAdmin)