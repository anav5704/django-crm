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


def delete(req, key):
    if req.user.is_authenticated:
        customer  = Customer.objects.get(id=key)
        customer.delete()

        messages.success(req, "Customer successfully deleted!")
        return redirect("home")
    else:
        messages.error(req, "Oops, something went wrong!")
        return redirect("home")
    
def create(req):
        if req.method == "POST":
            Customer.objects.create(
                firstName = req.POST["fname"],
                lastName = req.POST["lname"],
                email = req.POST["email"],
                phone = req.POST["phone"],
                city = req.POST["city"],
                country = req.POST["country"],
            )

            # mock_users_data = [
            #     {"firstName": "John", "lastName": "Doe", "email": "john.doe@example.com", "phone": "1234567890", "city": "City1", "country": "Country1"},
            #     {"firstName": "Jane", "lastName": "Doe", "email": "jane.doe@example.com", "phone": "9876543210", "city": "City2", "country": "Country2"},
            #     {"firstName": "Alice", "lastName": "Smith", "email": "alice.smith@example.com", "phone": "5551234567", "city": "City3", "country": "Country3"},
            #     {"firstName": "Bob", "lastName": "Johnson", "email": "bob.johnson@example.com", "phone": "4449876543", "city": "City4", "country": "Country4"},
            #     {"firstName": "Charlie", "lastName": "Brown", "email": "charlie.brown@example.com", "phone": "7778889999", "city": "City5", "country": "Country5"},
            # ]

            # for user_data in mock_users_data:
            #     Customer.objects.create(**user_data)

            messages.success(req, "Customer was successfully added!")
            return redirect("home")

        else:
            return render(req, "create.html", {})


def update(req, key):
    customer = Customer.objects.get(id=key)
    if req.method == "POST":
        if req.user.is_authenticated:
            customer.firstName = req.POST["fname"]
            customer.lastName = req.POST["lname"]
            customer.email = req.POST["email"]
            customer.phone = req.POST["phone"]
            customer.city = req.POST["city"]
            customer.country = req.POST["country"]

            customer.save()

            messages.success(req, "Customer successfully updated!")
            return redirect("home")
        else:
            messages.error(req, "Oops, something went wrong!")
            return redirect("home")
    else:
        return render(req, "update.html", {"customer": customer})

    

