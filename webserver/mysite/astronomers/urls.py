from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_astronomer, name="login"),  
]