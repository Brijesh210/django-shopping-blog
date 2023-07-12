from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# overriding the django admin
admin.site.register(User, UserAdmin)
