from django.contrib import admin

from .models import CustomUser
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["age","mail","username","mobile", "is_staff"]

admin.site.register(CustomUser,CustomUserAdmin)
