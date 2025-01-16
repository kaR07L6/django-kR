from django.contrib import admin
from .models import Sche

admin.site.register(Sche)


class ScheAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "description")
