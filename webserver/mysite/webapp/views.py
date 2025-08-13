from django.shortcuts import render
from django.http import HttpResponse
import subprocess

def home(request):
    return render(request, 'webapp/home.html')

def contact(request):
    return render(request, 'webapp/contact.html')
