from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse
from .models import Movie, Director, Log
from .forms import DirectorForm, MovieForm, LogForm
from .models import Event
from .forms import EventForm


def event_list(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()

    events = Event.objects.all()
    return render(request, 'schedulemyapp/event_list.html', {'form': form, 'events': events})


class IndexView(generic.ListView):
    template_name = "schedulemyapp/index.html"
    context_object_name = "movie_list"
    queryset = Movie.objects.all()

    # def index(request):
    # movie_list = Movie.objects.all()
    # return render(request, 'myapp/index.html', {'movie_list': movie_list})


class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = "schedulemyapp/detail.html"


class RegisterDirectorView(generic.CreateView):
    model = Director
    form_class = DirectorForm
    template_name = "schedulemyapp/register.html"

    def get_success_url(self):
        return reverse("schedulemyapp:registermovie")


class RegisterMovieView(generic.CreateView):
    model = Movie
    form_class = MovieForm
    template_name = "schedulemyapp/register.html"

    def get_success_url(self):
        return reverse("schedulemyapp:movie_detail", kwargs={"pk": self.object.pk})


class WritingLogView(generic.CreateView):
    model = Log
    form_class = LogForm
    template_name = "schedulemyapp/register.html"

    def get_success_url(self):
        return reverse(
            "schedulemyapp:movie_detail", kwargs={"pk": self.object.movie.pk}
        )


class UpdateLogView(generic.UpdateView):
    model = Log
    form_class = LogForm
    template_name = "myapp/register.html"

    def get_success_url(self):
        return reverse("myapp:movie_detail", kwargs={"pk": self.object.movie.pk})


# もしもFunction-viewで書くなら以下の通り


def updatelog(request, pk):
    obj = get_object_or_404(Log, id=pk)
    if request.method == "POST":
        form = LogForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("myapp:movie_detail", pk=obj.movie.pk)
    else:
        form = LogForm(instance=obj)
        return render(request, "myapp/register.html", {"form": form})


class DeleteLogView(generic.DeleteView):
    model = Log

    def get_success_url(self):
        return reverse("myapp:movie_detail", kwargs={"pk": self.object.movie.pk})


# ここからFunction-view


def deletelog(request, pk):
    obj = get_object_or_404(Log, id=pk)
    movie_id = obj.movie.pk
    if request.method == "POST":
        obj.delete()
        return redirect("myapp:movie_detail", pk=movie_id)
    context = {"obj": obj}
    return render(request, "myapp/delete.html", context)


class DeleteMovieView(generic.DeleteView):
    model = Movie

    def get_success_url(self):
        return reverse("myapp:index")


# ここからFunction-view


def deletemovie(request, pk):
    obj = get_object_or_404(Movie, id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("myapp:index")
    context = {"obj": obj}
    return render(request, "myapp/delete.html", context)


def writingthismovielog(request, movie_id):
    obj = get_object_or_404(Movie, id=movie_id)
    form = LogForm({"movie": obj})
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            l = form.save(commit=False)
            l.save()
            return redirect("myapp:movie_detail", pk=l.movie.pk)
    else:
        return render(request, "myapp/register.html", {"form": form})
