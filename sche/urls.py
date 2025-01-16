from django.urls import path
from . import views
from .views import ScheList, ScheDetail, ScheCreate, ScheUpdate, ScheDelete

urlpatterns = [
    path("", ScheList.as_view(), name="list"),
    path("detail/<int:pk>", ScheDetail.as_view(), name="detail"),
    path("create/", ScheCreate.as_view(), name="create"),
    path("update/<int:pk>", ScheUpdate.as_view(), name="update"),
    path("delete/<int:pk>", ScheDelete.as_view(), name="delete"),
]
