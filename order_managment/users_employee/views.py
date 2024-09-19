from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import LoginUserEmployeeForm, ProfileUserEmployeeForm, UserPasswordChangeForm


class LoginUserEmployee(LoginView):
    """Авторизация сотрудников"""
    forms_class = LoginUserEmployeeForm
    template_name = 'registration/login.html'
    extra_context = {'title': 'Авторизация'}


class ProfileUser(LoginRequiredMixin, UpdateView):
    """Страница профиля сотрудников"""
    model = get_user_model()
    form_class = ProfileUserEmployeeForm
    template_name = 'users_employee/profile_employee.html'
    extra_context = {'title': "Профиль сотрудника"}

    def get_success_url(self):
        return reverse_lazy('users_employee:profile_employee')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    """Изменить пароль"""
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users_employee:password_change_done")
    template_name = 'users_employee/password_change_form.html'
