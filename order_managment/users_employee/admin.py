"""
Административная конфигурация для модели UserEmployee.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserEmployee

admin.site.register(UserEmployee, UserAdmin)
