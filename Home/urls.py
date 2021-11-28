from typing import ValuesView
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from Home import views

urlpatterns = [
    path("",views.index,name='Home'),
    path("test",views.test,name='Home'),
    path("contact",views.contact,name='Home'),
    path("about",views.about,name="Home"),
    
]
