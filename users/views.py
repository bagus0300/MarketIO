from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib import messages

# TODO:
# add messages
# add error handling
# redirect to next page
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.info(request, "Successfully signed up!")
            return redirect('home')
        print(dict(form.errors))    
        for e in form.errors:
            print(e)
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
                messages.info(request, "Successfully logged in!")
                return redirect('home')
        return render(request, 'users/login.html', {'form':form})
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "Successfully logged out!")
    return redirect('home')