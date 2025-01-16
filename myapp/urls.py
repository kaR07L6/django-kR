from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
    path("", views.index, name="index"),  # アプリのトップページ
    path("page/create/", views.page_create, name="page_create"),
    path("pages/", views.page_list, name="page_list"),
]
