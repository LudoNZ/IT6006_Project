from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = CustomUser

    list_display = [
        "username",
        "email",
        "age",
    ]

    #when editing, what are data afields avaialable for existing user
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age", )}),)

    # when creating, what are the data fields required for the new user
    add_fieldsets = ((None, {"fields": ("email","username","password1","password2","age", )}),)

admin.site.register(CustomUser, CustomUserAdmin)
