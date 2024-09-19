from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from django.urls import path, reverse_lazy

from . import views

app_name = "users_employee"


urlpatterns = [
    path('', views.LoginUserEmployee.as_view(), name='login'), #http://127.0.0.1:8000/
    path('logout/', LogoutView.as_view(), name='logout'),

    path('password-change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(
         template_name='users_employee/password_change_done.html'),
         name='password_change_done'),

    path('password-reset/',
         PasswordResetView.as_view(
            template_name='users_employee/password_reset_form.html',
            email_template_name='users_employee/password_reset_email.html',
            success_url=reverse_lazy("users_employee:password_reset_done")
         ),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name='users_employee/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
            template_name='users_employee/password_reset_confirm.html',
            success_url=reverse_lazy("users_employee:password_reset_complete"),
         ),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='users_employee/password_reset_complete.html'),
         name='password_reset_complete'),

    path('profile_employee/', views.ProfileUser.as_view(), name='profile_employee'), #http://127.0.0.1:8000/profile_employee/
]
