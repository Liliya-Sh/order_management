"""
Конфигурация ASGI для проекта order_managment.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'order_managment.settings')

application = get_asgi_application()
