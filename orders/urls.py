from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_orders, name="my_orders"),
    path("success/", views.success_view, name="success"),
]