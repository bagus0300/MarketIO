from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, CreateUserAddressForm
from django.contrib import messages
from .models import UserAddress
from django.http import HttpResponse
from django.template.loader import render_to_string


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
    addresses = UserAddress.objects.filter(user=request.user).order_by("-is_default")
    if request.method == "POST":
        if request.GET.get("delete"):
            address = UserAddress.objects.get(id=request.GET.get("delete"))
            address.delete()
            response = HttpResponse()
            response.headers["HX-Redirect"] = "/account/addresses/"
            messages.info(request, "Successfully deleted address!")
            return response
        elif request.GET.get("set_default"):
            address = UserAddress.objects.get(id=request.GET.get("set_default"))
            previous_default = UserAddress.objects.get(
                user=request.user, is_default=True
            )
            previous_default.is_default = False
            previous_default.save()
            address.is_default = True
            address.save()
            print(address.id)
            print(previous_default.id)
            # RENDERS HTML FILES AS STRINGS FOR HTMX OOB-SWAP
            template1 = render_to_string(
                "partials/_is-not-default-address.html", {"address": previous_default}
            )
            template2 = render_to_string(
                "partials/_is-default-address.html", {"address": address}
            )
            # RETURN BOTH TEMPLATES AS ONE STRING SO HTMX CAN SWAP THEM
            return HttpResponse(template1 + template2)
        address = UserAddress(user=request.user)
        form = CreateUserAddressForm(request.POST, instance=address)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect("account_addresses")

    context = {"addresses": addresses, "counties": UserAddress.COUNTIES}
    return render(request, "account/addresses.html", context)
