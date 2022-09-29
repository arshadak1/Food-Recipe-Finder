from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('login', views.signin, name="sign-in"),
    path('sign-up', views.signup, name="sign-up"),
    path('sign-out', views.signout, name="sign-out"),


    
]
