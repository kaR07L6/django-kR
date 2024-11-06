from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]