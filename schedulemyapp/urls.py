from django.urls import path
from . import views

app_name = "schedulemyapp"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("movie/<int:pk>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path(
        "register/director/",
        views.RegisterDirectorView.as_view(),
        name="registerdirector",
    ),
    path("register/movie/", views.RegisterMovieView.as_view(), name="registermovie"),
    path("writing/log/", views.WritingLogView.as_view(), name="writinglog"),
    path("update/log/<int:pk>/", views.UpdateLogView.as_view(), name="updatelog"),
    path("delete/log/<int:pk>/", views.deletelog, name="deletelog"),
    path("delete/movie/<int:pk>/", views.deletemovie, name="deletemovie"),
    path('', views.event_list, name='event_list'),
]
