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
