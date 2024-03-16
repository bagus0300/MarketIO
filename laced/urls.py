from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from core import views as core_views
from users import views as user_views
from checkout import views as checkout_views
from products import views as product_views
from cart import views as cart_views
from marketing import views as marketing_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", core_views.home_view, name="home"),
    path("login/", user_views.login_view, name="login"),
    path("logout/", user_views.logout_view, name="logout"),
    path("signup/", user_views.signup_view, name="signup"),
    path("account/", user_views.account_view, name="account"),
    path(
        "account/addresses/",
        user_views.account_addresses_view,
        name="account_addresses",
    ),
    path("account/orders/", user_views.account_orders_view, name="account_orders"),
    path(
        "account/favourites/",
        user_views.account_favourites_view,
        name="account_favourites",
    ),
    path("products/", product_views.products_view, name="products"),
    path("products/add", product_views.add_product, name="add_product"),
    path(
        "products/edit/<int:product_id>",
        product_views.edit_product,
        name="edit_product",
    ),
    path(
        "products/delete/<int:product_id>",
        product_views.delete_product,
        name="delete_product",
    ),
    path(
        "products/<int:product_id>/",
        product_views.product_detail_view,
        name="product_detail",
    ),
    path("products/add_to_cart/", cart_views.add_to_cart, name="add_to_cart"),
    path("cart/", cart_views.cart_view, name="cart"),
    path(
        "cart/update_cart_quantity/<int:cart_item_id>/<int:quantity>/",
        cart_views.update_cart_quantity,
        name="update_cart_quantity",
    ),
    path(
        "cart/remove_from_cart/<int:cart_item_id>/",
        cart_views.remove_from_cart,
        name="delete_cart_item",
    ),
    path(
        "products/<int:product_id>/favourite/",
        user_views.add_remove_user_favourite,
        name="favourite",
    ),
    path("checkout/", checkout_views.checkout_view, name="checkout"),
    path(
        "checkout/confirmation/",
        checkout_views.checkout_confirmation_view,
        name="confirmation",
    ),
    path(
        "checkout/change_address/",
        checkout_views.checkout_change_address,
        name="checkout_change_address",
    ),
    path(
        "create_payment_intent/",
        checkout_views.create_payment_intent,
        name="create_payment_intent",
    ),
    path(
        "add_payment_intent_address/",
        checkout_views.add_payment_intent_address,
        name="add_payment_intent_address",
    ),
    path("stripe_webhook/", checkout_views.stripe_webhook, name="stripe_webhook"),
    path("subscribe/", marketing_views.subscribe, name="subscribe"),
    path("__debug__/", include("debug_toolbar.urls")),
]

# USED TO SERVE MEDIA FILES IN DEVELOPMENT
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
