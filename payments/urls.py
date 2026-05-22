from django.urls import path
from . import views

urlpatterns = [
    path("", views.payment_view, name="payment"),
    path("success/", views.success_view, name="success"),
]