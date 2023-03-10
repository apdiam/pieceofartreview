from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST or None)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("main:home")
    else:
        form = RegistrationForm()
    return render(request, "accounts/register.html", {"form": form})
