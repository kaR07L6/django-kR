from django.db import models
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name="参加登録")

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name="イベント登録")
    watch_date = models.DateField()
    director = models.ForeignKey(
        Director, on_delete=models.CASCADE, verbose_name="参加登録", related_name="movie"
    )

    def __str__(self):
        return self.title


class Log(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, verbose_name="イベント登録", related_name="log"
    )

    def __str__(self):
        return self.text
