from django.shortcuts import get_object_or_404, render, redirect
from .forms import BoardForm
from .models import Board


def index(request):
    boards = Board.objects.all().order_by("-updated_at")
    return render(request, "index.html", {"boards": boards})


def new(request):
    form = BoardForm()
    return render(request, "new.html", {"form": form})


def create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app:index")
    else:
        form = BoardForm()
    return render(request, "new.html", {"form": form})


def show(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, "show.html", {"board": board})


def edit(request, pk):
    board = Board.objects.get(pk=pk)
    form = BoardForm(instance=board)
    return render(request, "edit.html", {"form": form, "board": board})


def update(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect("app:show", pk=pk)
    else:
        form = BoardForm(instance=board)
    return render(request, "edit.html", {"form": form, "board": board})


def delete(request, pk):
    print(f"Received pk={pk}")
    board = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        board.delete()
        return redirect("app:index")
    return redirect("app:index")



