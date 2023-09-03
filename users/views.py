from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm

# TODO:
# add messages
# add error handling
# redirect to next page
def signup_view(request):
    if request.method == 'GET':
        form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'users/signup.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print('Wwowoowowo')
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'users/login.html', {'form':form})
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')