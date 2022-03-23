from django.contrib import admin
from .models import *


@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    list_display = ['step']

