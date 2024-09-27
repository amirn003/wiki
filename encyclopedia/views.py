from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django import forms
from . import util
import random

class ArticleForm(forms.Form):
    title = forms.CharField(label="Title",widget=forms.TextInput(attrs={"id": "title"}))
    content = forms.CharField(label="Content", widget=forms.Textarea)

    content.widget.attrs.update({"id": "content"})

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "random_article": random.choice(util.list_entries())
    })

def display_page(request, name):
    return render(request, f"entries/{name}.md")

def add(request):
    return render(request, "encyclopedia/add.html", {
        "form": ArticleForm()
    })

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
