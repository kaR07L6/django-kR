from django.urls import path
from . import views

#
urlpatterns = [
    path("index/", views.index, name="index"),  # 一覧、トップページ
    path("", views.new, name="new"),  # 新規投稿
]
