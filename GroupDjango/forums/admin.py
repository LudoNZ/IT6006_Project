from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category, Forum

# Register your models here.

admin.site.register(Category)
admin.site.register(Forum)
