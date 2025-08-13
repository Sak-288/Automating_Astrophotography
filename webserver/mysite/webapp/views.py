from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
import subprocess

def home(request):
    return render(request, 'webapp/home.html')

def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        contact.name = name
        contact .email = email
        contact.subject = subject
        contact.save()
        return HttpResponse('<h1>Thanks for contacting us !</h1>')
    return render(request, 'webapp/contact.html')
