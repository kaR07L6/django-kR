from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
