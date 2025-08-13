from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import *
from django.contrib.auth.forms import UserCreationForm

def login_astronomer(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        pass
        return render(request, 'registration/login.html')

def logout_astronomer(request):
    logout(request)
    return redirect('home')

def register_astronomer(request):
    return render(request, 'registration/register_astronomer.html', {})
