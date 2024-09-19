from django.shortcuts import redirect
from django.urls import reverse


def is_director(user):
    """Право доступа к страницам сайта должность сотрудника:директор"""
    return user.groups.filter(name='Директор').exists()


def is_delivery(user):
    """Право доступа к страницам сайта должность сотрудника:доставщики"""
    return user.groups.filter(name='Доставщики').exists() or is_director(user)


def is_cook(user):
    """Право доступа к страницам сайта, должность сотрудника:повара"""
    return user.groups.filter(name='Повара').exists() or is_director(user)


def user_passes_test(test_func):
    """Декоратор для проверки прав доступа пользователя."""
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user) or request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            else:
                # Перенаправление на страницу профиля, если доступ запрещен
                return redirect(reverse('users_employee:profile_employee'))
        return _wrapped_view
    return decorator


# Используйте user_passes_test для создания декоратора
is_cook_decorator = user_passes_test(is_cook)
is_delivery_decorator = user_passes_test(is_delivery)
