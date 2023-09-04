from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _


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

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    """
    Product category model for storing product categories.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    """
    Product image model for storing product images.
    """

    image = models.ImageField(_("Image"), upload_to="media/")
    product = models.ForeignKey(
        "core.Product", on_delete=models.CASCADE, null=True, blank=True, default=None
    )
