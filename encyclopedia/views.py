from django.shortcuts import render, redirect, reverse
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
        context = request.POST.get("content")
        print(context)
        #for entry in util.list_entries():
        if title.upper() in util.list_entries():
            return HttpResponseBadRequest(f"<h1>'{title}' is already in the encyclopedia!<h1>")
        else:
            util.save_entry(title, context)
            #display_page(request, title)
            return redirect(f'/wiki/{title}')
            # return redirect(reverse('article_path', args=[title]))
