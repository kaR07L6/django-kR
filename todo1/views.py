from django.http import HttpResponse
from todo1 import models
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    # テンプレートにデータを渡す
    all_todo = models.Todo.objects.all()

    # return HttpResponse(all_todo)
    context = {"all_todo": all_todo}
    return render(request, "todo1/list.html", context)


def edit(request):
    return HttpResponse("Hello, world. You're at the list edit.")


def register(request):
    title = request.POST.get("title")
    if title is None or title == "":
        return HttpResponseRedirect(reverse("todo1:list"))
    # データを登録する
    t = models.Todo()
    t.title = title
    t.save()
    return HttpResponseRedirect(reverse("todo1:list"))
    # return HttpResponse(all_todo)
