from django.forms import ModelForm
from .models import Page


class PageForm(ModelForm):  # PageFormは,日記のページ用のホーム
    class Meta:
        model = Page
        fields = ["title", "body", "page_date"]  # []の中はユーザーが入力する項目
