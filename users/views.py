from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, CreateUserAddressForm
from django.contrib import messages
from .models import UserAddress
from django.http import HttpResponse
from django.template.loader import render_to_string
from products.models import Product
from users.models import UserFavourite
from checkout.models import Order
from django.contrib.auth.decorators import login_required


def signup_view(request):
    """
    View function for user signup.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
    # If user is already authenticated, redirect to home
    if request.user.is_authenticated:
        return redirect("home")
    # If the request method is POST, process the form data
    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.info(request, "Successfully signed up!")
            if request.GET.get("next"):
                return redirect(request.GET.get("next"))
            return redirect("home")
        else:
            # If form is not valid, render the signup template with the form and errors
            return render(request, "users/signup.html", {"form": form})
    # If the request method is GET, render the signup template with a blank form
    else:
        form = CustomUserCreationForm()

    return render(request, "users/signup.html", {"form": form})


def login_view(request):
    """
    View function for handling user login.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    """
    if request.user.is_authenticated:
        return redirect("home")
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
    """
    Logs out the user and redirects to the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the home page.

    """
    logout(request)
    messages.info(request, "Successfully logged out!")
    return redirect("home")


def account_addresses_view(request):
    """
    View function for handling user addresses.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    addresses = UserAddress.objects.filter(user=request.user).order_by("-is_default")
    if request.method == "GET":
        # IF USER IS EDITING AN ADDRESS
        if request.GET.get("edit"):
            address = UserAddress.objects.get(id=request.GET.get("edit"))
            isEditing = True
            return render(
                request,
                "partials/_add-address-form.html",
                {
                    "address": address,
                    "isEditing": isEditing,
                    "counties": UserAddress.COUNTIES,
                },
            )
    if request.method == "POST":
        # IF USER IS EDITING AN ADDRESS
        if request.GET.get("edit"):
            address = UserAddress.objects.get(id=request.GET.get("edit"))
            set_default = False
            if address.is_default == True:
                set_default = True
            print(address.is_default)
            form = CreateUserAddressForm(request.POST, instance=address)
            if form.is_valid():
                address.name = form.cleaned_data["name"]
                address.address_line_1 = form.cleaned_data["address_line_1"]
                address.address_line_2 = form.cleaned_data["address_line_2"]
                address.city = form.cleaned_data["city"]
                address.county = form.cleaned_data["county"]
                address.eircode = form.cleaned_data["eircode"]
                if set_default == True:
                    address.is_default = True
                address.save()
                return redirect("/account/addresses")
        # IF USER IS DELETING AN ADDRESS
        if request.GET.get("delete"):
            address = UserAddress.objects.get(id=request.GET.get("delete"))
            # IF USER IS DELETING THEIR DEFAULT ADDRESS, SET THE FIRST ADDRESS IN THE LIST TO DEFAULT
            if address.is_default:
                address.delete()
                # GET ALL ADDRESSES EXCEPT THE ONE BEING DELETED
                addresses = UserAddress.objects.exclude(id=request.GET.get("delete"))
                if addresses.exists():
                    new_default = addresses.first()
                    new_default.is_default = True
                    new_default.save()
            # IF USER IS DELETING AN ADDRESS THAT IS NOT THEIR DEFAULT
            else:
                address.delete()
            # RETURN A BLANK RESPONSE WITH A HEADER THAT HTMX CAN USE TO REDIRECT
            response = HttpResponse()
            response.headers["HX-Redirect"] = "/account/addresses/"
            messages.info(request, "Successfully deleted address!")
            return response
        # IF USER IS SETTING AN ADDRESS TO DEFAULT
        elif request.GET.get("set_default"):
            address = UserAddress.objects.get(id=request.GET.get("set_default"))
            # IF USER HAS A DEFAULT ADDRESS, SET IT TO FALSE
            if UserAddress.objects.filter(user=request.user, is_default=True).exists():
                previous_default = UserAddress.objects.get(
                    user=request.user, is_default=True
                )
                previous_default.is_default = False
                previous_default.save()
            address.is_default = True
            address.save()
            # RENDERS HTML FILES AS STRINGS FOR HTMX OOB-SWAP
            if previous_default:
                template1 = render_to_string(
                    "partials/_is-not-default-address.html",
                    {"address": previous_default},
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
            if not UserAddress.objects.filter(
                is_default=True, user=request.user
            ).exists():
                address.is_default = True
            address.save()
            return redirect(request.META.get("HTTP_REFERER"))

    context = {"addresses": addresses, "counties": UserAddress.COUNTIES}
    return render(request, "account/addresses.html", context)


@login_required
def add_remove_user_favourite(request, product_id):
    """
    Add or remove a product from the user's favorites.

    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to add or remove.

    Returns:
        HttpResponse: The rendered HTML response containing the updated favorite button.

    """
    product = Product.objects.get(id=product_id)
    product_favourite = UserFavourite.objects.filter(user=request.user, product=product)
    if len(product_favourite) > 0:
        product_favourite[0].delete()
        is_favourite = False
    else:
        UserFavourite.objects.create(user=request.user, product_id=product_id)
        is_favourite = True

    context = {
        "is_favourite": is_favourite,
        "product": product,
    }
    return render(request, "products/partials/_favourite_button.html", context)


@login_required
def account_view(request):
    """
    Renders the account overview page.

    Args:
        request: The HTTP request object.

    Returns:
        The rendered account overview page.
    """
    return render(request, "account/overview.html")


@login_required
def account_orders_view(request):
    """
    View function to display the orders associated with the current user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    orders = Order.objects.filter(user=request.user).order_by("-date_created")
    context = {
        "orders": orders,
    }
    return render(request, "account/orders.html", context)


@login_required
def account_favourites_view(request):
    """
    View function that renders the user's favourite products.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    favourite_products = UserFavourite.objects.filter(user=request.user)
    return render(
        request, "account/favourites.html", {"favourite_products": favourite_products}
    )
