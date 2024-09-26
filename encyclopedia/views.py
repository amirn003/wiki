from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "random_article": random.choice(util.list_entries())
    })

def display_page(request, name):
    return render(request, f"entries/{name}.md")

def add(request):
    return render(request, "encyclopedia/add.html")

def new_entry(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if not title:
            return HttpResponseBadRequest(f"<h1>Please enter a title!</h1>")
        if  title in util.list_entries():
            return HttpResponseBadRequest(f"<h1>'{title}' is already in the encyclopedia!</h1>")

        util.save_entry(title, content)
        return redirect(f'/wiki/{title}')
