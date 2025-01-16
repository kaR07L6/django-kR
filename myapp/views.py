from django.shortcuts import render, redirect
from django.views import View
from .forms import PageForm
from .models import Page
from datetime import datetime
from zoneinfo import ZoneInfo


class IndexView(View):
    def get(self, request):
        datetime_now = datetime.now(ZoneInfo("Asia/Tokyo")).strftime(
            "%Y年%m月%d日 %H:%M:%S"
        )
        return render(
            request, "myapp/index.html", {"datetime_now": datetime_now}
        )  # 画面のレスポンスを返す,返す画面のhtmlファイル


class PageCreateView(View):
    def get(self, request):  # データを入力する画面を表示
        form = PageForm()
        return render(request, "myapp/event_form.html", {"form": form})

    def post(self, request):
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("myapp:index")
        return render(request, "myapp/event_form.html", {"form": form})


class PageListView(View):
    def get(self, request):
        page_list = Page.objects.all()
        return render(request, "myapp/page_list.html", {"page_list": page_list})


index = IndexView.as_view()
page_create = PageCreateView.as_view()
page_list = PageListView.as_view()
