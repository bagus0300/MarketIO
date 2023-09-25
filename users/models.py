from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db.models import Q, UniqueConstraint

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Summary:
            Creates and saves a User with the given email, first/last name and password.

        Args:
            email (str): User's email address.
            first_name (str): User's first name.
            last_name (str): User's last name.
            password (str): User's password.

        Returns:
            user: User object.

        """
        #  IF VALID EMAIL IS NOT PROVIDED, RAISE ERROR
        if not email:
            raise ValueError("Users must have an email address")
        #  CREATE USER OBJECT
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        #  SET PASSWORD
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        """
        Summary:
            Creates and saves a superuser with the given email, first/last name and password.

        Args:
            email (str): User's email address.
            first_name (str): User's first name.
            last_name (str): User's last name.
            password (str): User's password.

        Returns:
            user: User object with superuser permissions.
        """
        # IF VALID EMAIL IS NOT PROVIDED, RAISE ERROR
        if not email:
            raise ValueError("Superusers must have an email address")
        #  CREATE SUPERUSER OBJECT
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    # USERMANAGER CLASS DEFINED ABOVE
    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class UserFavourite(models.Model):
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="favourites",
    )
    product = models.ForeignKey(
        "core.Product", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"{self.product.name}"


class UserAddress(models.Model):
    COUNTIES = [
        ('carlow', 'Carlow'),
        ('cavan', 'Cavan'),
        ('clare', 'Clare'),
        ('cork', 'Cork'),
        ('donegal', 'Donegal'),
        ('dublin', 'Dublin'),
        ('galway', 'Galway'),
        ('kerry', 'Kerry'),
        ('kildare', 'Kildare'),
        ('kilkenny', 'Kilkenny'),
        ('laois', 'Laois'),
        ('leitrim', 'Leitrim'),
        ('limerick', 'Limerick'),
        ('longford', 'Longford'),
        ('louth', 'Louth'),
        ('mayo', 'Mayo'),
        ('meath', 'Meath'),
        ('monaghan', 'Monaghan'),
        ('offaly', 'Offaly'),
        ('roscommon', 'Roscommon'),
        ('sligo', 'Sligo'),
        ('tipperary', 'Tipperary'),
        ('waterford', 'Waterford'),
        ('westmeath', 'Westmeath'),
        ('wexford', 'Wexford'),
        ('wicklow', 'Wicklow')
    ]

    user = models.ForeignKey("User", on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    address_line_1 = models.CharField(max_length=500)
    address_line_2 = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500)
    county = models.CharField(max_length=50, choices=COUNTIES)
    eircode = models.CharField(max_length=8)
    is_default = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(fields=["user", "is_default"], condition=Q(is_default="True"), name="unique_default_address")
        ]