# webapp/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),        # for root URL (e.g. /)
    path('home/', views.home, name='home'),   # for /home URL
    path('contact.html', views.contact, name='contact'),   # for /home URL
    path('contact_successful.html', views.contact_successful, name='contact_successful'),   # for /home URL
    path('test_for_animation.pug', views.test_for_animation, name='test_for_animation'),   # for /home URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)