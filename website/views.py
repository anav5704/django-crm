from django.contrib.auth import authenticate, login as authLogin, logout as authLogout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Customer

def home(req):
    customers = Customer.objects.all

    if req.method == "POST":
        username = req.POST["username"]
        passwd = req.POST["passwd"]

        user = authenticate(req, username=username, password=passwd)

        if user is not None:
            authLogin(req, user)
            messages.success(req, "You've been successfully logged in!")
            return redirect("home")
        else:
            messages.error(req, "Oops, something went wrong!")
            return redirect("home")

    else:
        return render(req, "home.html", {"customers": customers})


def logout(req):
    authLogout(req)
    messages.success(req, "You've been successfully logged out!")
    return redirect("home")


def customer(req, key):
    if req.user.is_authenticated:
        customer = Customer.objects.get(id=key)
        return render(req, "customer.html", {"customer": customer})
