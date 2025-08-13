from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'webapp/home.html')

def contact(request):
    if request.method == "POST":
        subject = request.POST['subject']
        name = request.POST['name']
        email = request.POST['email']

        send_mail(f'Message from {name}', subject, 'settings.EMAIL_HOST_USER', [email], fail_silently=False)
        return HttpResponse('<h1>Thanks for contacting us !</h1>')
    return render(request, 'webapp/contact.html')
