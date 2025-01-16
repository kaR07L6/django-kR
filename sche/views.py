from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Sche


class ScheList(ListView):
    model = Sche
    context_object_name = "events"
    template_name = "sche/event_list.html"


def index(request):
    return render(request, "sche/event_list.html")


class ScheDetail(DetailView):
    model = Sche
    context_object_name = "event"
    template_name = "sche/event_detail.html"


class ScheCreate(CreateView):
    model = Sche
    fields = "__all__"
    template_name = "sche/event_form.html"
    success_url = reverse_lazy("list")


class ScheUpdate(UpdateView):
    model = Sche
    fields = "__all__"
    success_url = reverse_lazy("list")
    template_name = "sche/event_form.html"


class ScheDelete(DeleteView):
    model = Sche
    context_object_name = "event"
    success_url = reverse_lazy("list")
    template_name = "sche/event_confirm_delete.html"
