"""
Формы для аутентификации и управления учетными записями сотрудников.
"""

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


class LoginUserEmployeeForm(AuthenticationForm): # pylint: disable=too-few-public-methods
    """Форма для аутентификации сотрудников."""

    username = forms.CharField(label="Логин",
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta: # pylint: disable=too-few-public-methods
        """Метаданные для формы аутентификации."""
        model = get_user_model()
        fields = ['username', 'password']


class ProfileUserEmployeeForm(forms.ModelForm): # pylint: disable=too-few-public-methods
    """Форма для редактирования профиля сотрудника."""

    username = forms.CharField(disabled=True,
                               label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True,
                            label='E-mail',
                            widget=forms.TextInput(attrs={'class': 'form-input'}))
    position = forms.CharField(disabled=True,
                               label='Должность',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta: # pylint: disable=too-few-public-methods
        """Метаданные для формы редактирования профиля."""

        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'position', 'phone']
        labels = {'first_name': 'Имя',
                  'last_name': 'Фамилия',
                  'position': 'Должность',
                  'phone': 'Номер телефона',
                  }


class UserPasswordChangeForm(PasswordChangeForm): # pylint: disable=too-few-public-methods
    """Форма для изменения пароля пользователя."""

    old_password = forms.CharField(label="Старый пароль",
                                   widget=forms.TextInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label="Новый пароль",
                                    widget=forms.TextInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label="Подтверждение пароля",
                                    widget=forms.TextInput(attrs={'class': 'form-input'}))
