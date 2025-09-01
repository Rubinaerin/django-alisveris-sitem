# products/urls.py

from django.urls import path
from . import views

app_name = 'products' 

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:pk>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]