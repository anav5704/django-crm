from django.contrib.auth import authenticate, login as authLogin, logout as authLogout
from django.shortcuts import render, redirect
from django.contrib import messages

def home(req):
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
        return render(req, "home.html", {})
    
def logout(req):
    pass
