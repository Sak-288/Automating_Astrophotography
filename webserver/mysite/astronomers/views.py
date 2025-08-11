from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_astronomer(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome! You have been logged in successfully.')
            return redirect('home')
        else:
            messages.error(request, 'There was an error logging in, TRY AGAIN!')
            # return redirect('login')
    else:
        return render(request, 'registration/login.html', {})