from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from cart.models import CartItem
from orders.models import Order


def checkout_view(request):

    # ALL cart items
    cart_items = CartItem.objects.all()

    total = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == "POST":

        name = request.POST.get("name")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        now = timezone.now()

        for item in cart_items:

            Order.objects.create(
                product=item.product,
                quantity=item.quantity,
                customer_name=name,
                address=address,
                phone=phone,
                status="Pending",
                shipping_date=now + timedelta(days=1),
                delivery_date=now + timedelta(days=4),
            )

        # clear cart
        cart_items.delete()

        return redirect("/payments/")

    return render(request, "checkout/checkout.html", {
        "cart_items": cart_items,
        "total": total
    })