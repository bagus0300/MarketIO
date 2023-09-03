from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")

# class CustomLoginForm(AuthenticationForm):
#     email = 
#     class Meta:
#         model = User
#         fields = ("email", "password")