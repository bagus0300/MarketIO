from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'GET':
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form':form})

def login_view(request):
    return render(request, 'users/login.html')