from django.shortcuts import render, redirect
from .forms import EventForm
from django.urls import path
from django.http import HttpResponse
from . import views
from .models import Event

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
        
    else:
        form = EventForm()

    return render(request, "event/create_event.html", {"form": form})


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


urlpatterns = [
    path("", views.index, name="index"),
]


def event_list(request):
    return render(request, "event/event_list.html")


from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the event index.")


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventForm()
    return render(request, 'event/create_event.html', {'form': form})


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event/event_list.html', {'events': events})