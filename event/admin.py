from django.contrib import admin
from .models import Event



admin.site.register(Event)


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'description')

