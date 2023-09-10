from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _
import os


class Product(models.Model):
    """
    Product model for storing product information.
    Attributes:
        name (str): Product name
        sku (str): Product SKU (Stock Keeping Unit)
        - must be unique and exactly 6 numerical characters
        description (str): Product description
        category (str): Product category
        price (float): Product price, 2 decimal places

    """

    name = models.CharField(_("Product Name"), max_length=50)
    sku = models.CharField(
        _("SKU"),
        max_length=10,
        unique=True,
        help_text="SKU must be unique and exactly 6 numerical characters",
        validators=[
            RegexValidator(
                regex="[0-9]{6}", message="SKU must be exactly 6 numerical characters"
            )
        ],
    )
    description = models.TextField(_("Product Description"), max_length=500)
    category = models.ForeignKey(
        "core.ProductCategory",
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True,
        blank=True,
    )
    price = models.DecimalField(decimal_places=2, max_digits=10)
    sale_price = models.DecimalField(decimal_places=2, max_digits=10, default=False)
    is_featured = models.BooleanField(_("Featured Product?"), default=False)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    """
    Product category model for storing product categories.
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


def upload_to_product_img(instance, filename):
    """
    Defines the upload path for product images.
    """

    filename = os.path.basename(filename)
    return os.path.join("product_imgs", filename)


class ProductImage(models.Model):
    """
    Product image model for storing product images.
    """

    image = models.ImageField(_("Image"), upload_to=upload_to_product_img)
    product = models.ForeignKey(
        "core.Product", on_delete=models.SET_NULL, null=True, blank=True, default=None
    )


class ProductVariant(models.Model):
    """
    Product variant model for storing product variants.
    Defines the product size and quantity in stock.
    """

    SIZES = [
        ("5.5", "UK 5.5"),
        ("6", "UK 6"),
        ("6.5", "UK 6.5"),
        ("7", "UK 7"),
        ("7.5", "UK 7.5"),
        ("8", "UK 8"),
        ("8.5", "UK 8.5"),
        ("9", "UK 9"),
        ("9.5", "UK 9.5"),
        ("10", "UK 10"),
        ("10.5", "UK 10.5"),
        ("11", "UK 11"),
        ("12.5", "UK 12.5"),
        ("13", "UK 13"),
    ]
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    size = models.CharField(_("Size"), max_length=50, choices=SIZES)
    quantity = models.PositiveIntegerField(
        _("Qty in stock"), blank=True, default=0, null=True
    )

    def __str__(self):
        return f"{self.product.name}; {self.size}"


class CartItem(models.Model):
    item = models.ForeignKey("ProductVariant", on_delete=models.CASCADE)
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity}no. {self.item.product.name}"


class Cart(models.Model):
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, default=None, null=True, blank=True
    )
    session = models.CharField(max_length=32, default=None, null=True, blank=True)

    def add_item(self, product, quantity):
        cart_item = CartItem.objects.filter(item=product, cart=self)
        if cart_item.exists():
            cart_item = cart_item.first()
            cart_item.quantity = cart_item.quantity + quantity
            cart_item.save()
            return
        return CartItem.objects.create(item=product, cart=self, quantity=quantity)

    def remove_item(self, product):
        return CartItem.objects.get(item=product, cart=self).delete()

    def get_total_items(self):
        items = self.cartitem_set.all()
        total_quantity = 0
        for item in items:
            total_quantity += item.quantity
        return total_quantity

    def get_total_price(self):
        items = self.cartitem_set.all()
        total_price = 0
        for item in items:
            print(item)
            total_price += (item.quantity * item.item.product.price)
            print(total_price)
        return total_price
