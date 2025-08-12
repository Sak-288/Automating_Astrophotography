from django.urls import path
from . import views

urlpatterns = [
    path('login_astronomer', views.login_astronomer, name="login"),  
    path('logout_astronomer', views.logout_astronomer, name="logout"), 
]