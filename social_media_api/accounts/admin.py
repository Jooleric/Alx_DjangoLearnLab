from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    # extend fieldsets if you want to show bio & profile_picture in admin
    fieldsets = UserAdmin.fieldsets + (
        ('Extra', {'fields': ('bio', 'profile_picture', 'followers')}),
    )
