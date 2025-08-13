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

        send_mail(f'Message from {name}', subject, email, [settings.EMAIL_HOST_USER], fail_silently=False)
        return render(request, 'webapp/contact_successful.html')
    return render(request, 'webapp/contact.html')
