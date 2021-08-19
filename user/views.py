from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout

from django.contrib import messages


def register(request):

    form = UserRegisterForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully signed up")
        return redirect("index")

    context = {
        "form": form
    }
    return render(request, "register.html", context)


def login(request):
    form = UserLoginForm(request.POST or None)
    context = {

        "form": form
    }

    if form.is_valid():

        print("VALIDATED...")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        print(f"Username: ${username}")
        print(f"Password: ${password}")

        user = authenticate(username=username, password=password)
        print(user)
        if(user is None):
            messages.info(request, "Incorrect username or password")
            return render(request, "login.html", context)

        messages.info(request, "Succesfully logged in")
        auth_login(request, user)
        return redirect(("index"))

    return render(request, "login.html", context)


def log_out(request):
    logout(request)
    messages.success(request, "Successfully signed out")

    return redirect("index")
