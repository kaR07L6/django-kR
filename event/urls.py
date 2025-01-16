from django.urls import path
from django.contrib import admin
from . import views

app_name = "event"

urlpatterns = [
    path("", views.event_list, name="event_list"),
    path("event/", views.create_event, name="event_form"),
    path("admin/", admin.site.urls),
]

