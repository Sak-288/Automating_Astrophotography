from django.urls import path
from . import views

urlpatterns = [
    path('login_astronomer', views.login_astronomers, name="login"),  
]