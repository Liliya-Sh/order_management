"""
Тесты для приложения users_employee
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

UserEmployee = get_user_model()


class UserEmployeeTests(TestCase):
    """Тестирование пользователя на авторизацию и просмотр профиля"""

    def setUp(self):
        """Создаем тестового пользователя"""
        self.user = UserEmployee.objects.create_user(
            username='testuser',
            password='testpassword',
            position='Cook'
        )

    def test_login_user(self):
        """Тест на успешную авторизацию пользователя."""

        response = self.client.post(reverse('users_employee:login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            response.wsgi_request.user.is_authenticated)

    def test_view_profile(self):
        """Тест на просмотр профиля пользователя."""

        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('users_employee:profile_employee'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'users_employee/profile_employee.html')
        self.assertContains(response,
                            'Профиль')

    def test_view_profile_not_logged_in(self):
        """Тест на попытку просмотра профиля без авторизации."""
        response = self.client.get(reverse('users_employee:profile_employee'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,
                             f"{reverse('users_employee:login')}"
                             f"?next={reverse('users_employee:profile_employee')}")
