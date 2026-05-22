from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # homepage
    path('products/', views.product_list, name='product_list_all'),  # NEW
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]