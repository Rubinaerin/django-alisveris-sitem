# users/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    # Profil sayfanız için URL'yi buraya ekleyin
    path('profile/', views.user_profile, name='user_profile'),
    # Kayıt sayfası için URL'yi buraya ekleyin
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
]