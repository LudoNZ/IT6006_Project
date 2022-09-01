from django.contrib import admin
from .models import *

admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Content)
admin.site.register(Questions)