from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path("event/", include("event.urls")),  # event アプリの URL を追加
    path("admin/", admin.site.urls),
    # path("todo1/", include("todo1.urls")),
    # path('schedulemyapp/', include('schedulemyapp.urls')),
    # path("sche/", include("sche.urls")),
    # path("myapp/", include("myapp.urls")),
    path("", include("app.urls")),
]
