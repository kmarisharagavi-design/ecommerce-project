from django.shortcuts import render
from .models import Order


def my_orders(request):

    # get all orders
    orders = Order.objects.all().order_by("-id")

    return render(request, "orders/my_orders.html", {
        "orders": orders
    })


def success_view(request):
    return render(request, "orders/success.html")