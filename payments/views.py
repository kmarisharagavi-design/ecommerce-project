from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def payment_view(request):

    if request.method == "POST":
        return redirect("success")

    return render(request, "payments/payment.html")


def success_view(request):
    return render(request, "payments/success.html")