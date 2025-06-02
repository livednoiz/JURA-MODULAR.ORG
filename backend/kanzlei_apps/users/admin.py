from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User  # oder wie dein Modell heißt

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass
# Register your models here.
# This code registers the User model with the Django admin site using a custom UserAdmin class.