from django.db import models
import uuid


class Page(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID"
    )
    title = models.CharField(max_length=100, verbose_name="タイトル")
    body = models.TextField(max_length=1000, verbose_name="本文")
    page_date = models.DateField(verbose_name="日付")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="作成日時"
    )  # auto_now_add=Trueは,このデータが初めて作成された時の日時を保存
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="更新日時"
    )  # auto_now=Trueは,このデータが保存,更新される度にその時の日時を保存

    def __str__(self):
        return self.title
