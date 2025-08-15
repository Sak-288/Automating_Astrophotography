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

def contact_successful(request):
    return render(request, 'webapp/contact_successful.html')

def test_for_animation(request):
    t = 7
    t2_plus_1 = 2 * t + 1

    # Create lists of data for the template
    positive_lines = [{"i": i, "c": t + i, "dp": i / t} for i in range(1, t)]
    negative_lines = [{"i": i, "c": t - i, "dp": i / t} for i in range(1, t)]

    context = {
        "t": t,
        "t2_plus_1": t2_plus_1,
        "positive_lines": positive_lines,
        "negative_lines": negative_lines,
    }
    return render(request, "webapp/test_for_animation.html", context)