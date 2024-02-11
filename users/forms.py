from .models import User, UserAddress
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    """
    A custom form for creating a new user.

    Inherits from UserCreationForm and adds additional fields for email, first name, and last name.
    """

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")

class CreateUserAddressForm(ModelForm):
    """
    Form for creating a user address.

    Inherits from ModelForm and specifies the model to use and the fields to exclude.

    Attributes:
        model (UserAddress): The model to use for the form.
        exclude (list): The fields to exclude from the form.

    """
    class Meta:
        model = UserAddress
        exclude = ["user"]
