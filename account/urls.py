from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (dashboard, register, edit, user_list,
                    user_detail, user_follow)

urlpatterns = [
    # path('login/', views.user_login, name='login'),

    # # login / logout urls
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #
    # # change password urls
    # path('password-change/',
    #      auth_views.PasswordChangeView.as_view,
    #      name='password-change'),
    # path('password-change/done/',
    #      auth_views.PasswordChangeDoneView.as_view(),
    #      name='password_change_done'),
    #
    # # reset password urls
    # path('password-rest/',
    #      auth_views.PasswordResetView.as_view(),
    #      name='password-reset'),
    # path('password-reset/done/',
    #      auth_views.PasswordChangeDoneView.as_view(),
    #      name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>',
    #      auth_views.PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),
    # path('password-reset/complete',
    #      auth_views.PasswordResetCompleteView.as_view(),
    #      name='password_reset_complete'),
    path('', include('django.contrib.auth.urls')),
    path('', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('users', user_list, name='user_list'),
    path('users/follow/', user_follow, name='user_follow'),
    path('users/<username>/', user_detail, name='user_detail'),
]
