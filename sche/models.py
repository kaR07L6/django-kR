from django.db import models


class Sche(models.Model):
    title = models.CharField("イベント名", max_length=200)
    date = models.TextField("詳細")
    description = models.TextField("説明")

    def __str__(self):
        return self.title
