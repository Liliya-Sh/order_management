"""
Конфигурация приложения для управления учетными записями сотрудников.
"""

from django.apps import AppConfig


class UsersEmployeeConfig(AppConfig):
    """Конфигурация приложения для users_employee."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_employee'
