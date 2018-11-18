from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import login, logout, register, profile

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
        template_name='registration/reset_password_form.html'),
        name='password_reset'),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
        template_name='registration/reset_password_done.html'),
        name='password_reset_done'),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/reset_password_confirm.html'),
        name='password_reset_confirm'),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/reset_password_complete.html'),
        name='password_reset_complete'),
]