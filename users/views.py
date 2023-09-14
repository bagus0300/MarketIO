from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import UserAddress


# TODO:
# add error handling
# redirect to next page
def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.info(request, "Successfully signed up!")
            if request.GET.get("next"):
                return redirect(request.GET.get("next"))
            return redirect("home")
    return render(request, "users/signup.html")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "Successfully logged in!")
                if request.GET.get("next"):
                    return redirect(request.GET.get("next"))
                return redirect("home")
        return render(request, "users/login.html", {"form": form})
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    messages.info(request, "Successfully logged out!")
    return redirect("home")


def account_addresses_view(request):
    addresses = UserAddress.objects.filter(user=request.user)
    context = {
        "addresses":addresses,
        "counties":UserAddress.COUNTIES
    }
    return render(request, 'account/addresses.html', context)