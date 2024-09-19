"""
Контекстные процессоры для приложения users_employee, restaurant_ordering.
"""

from restaurant_ordering.utils import menu


def get_context(request):
    """Возвращает контекст для шаблонов, включая главное меню."""
    return {'mainmenu': menu}
