from django.shortcuts import render

from products.models import Product
from orders.models import Order
from users.models import CustomUser


def dashboard(request):

    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    total_users = CustomUser.objects.count()

    context = {
        "total_products": total_products,
        "total_orders": total_orders,
        "total_users": total_users,
    }

    return render(request, "admin_dashboard/dashboard.html", context)