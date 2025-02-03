from django.shortcuts import render, redirect
from .forms import MainForm
from .models import Main


#
def index(request):
    mains = Main.objects.all().order_by("updated_at")
    return render(request, "suntory/index.html", {"mains": mains})


def new(request):
    if request.method == "POST":
        form = MainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = MainForm()
    return render(request, "suntory/new.html", {"form": form})
