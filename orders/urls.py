# orders/urls.py

from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.create_order, name='order_checkout'),
    path('create/', views.create_order, name='create_order'),
    
    path('<int:order_id>/', views.order_detail, name='order_detail'), 
]