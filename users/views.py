from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import CustomUser


def login_view(request):

    error = None

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        # user check
        user = CustomUser.objects.filter(username=username).first()

        # user illa na create + encrypt password
        if not user:

            encrypted_password = make_password(password)

            user = CustomUser.objects.create(
                username=username,
                password=encrypted_password
            )

            request.session["user_id"] = user.id
            return redirect("/")

        # existing user password check
        if check_password(password, user.password):

            request.session["user_id"] = user.id
            return redirect("/")

        else:
            error = "Wrong password"

    return render(request, "users/login.html", {"error": error})