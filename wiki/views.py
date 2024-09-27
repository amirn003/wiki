from django.shortcuts import render, redirect
from django.http import HttpResponse
from encyclopedia import util
from django import forms


def index(request):
    return HttpResponse("Wiki Index!")

def search_by_title(request, name):
    if util.get_entry(name):
        read_entry = util.get_entry(name)
        return render(request, "wiki/article.html", {
            "name": name,
            "read_entry": read_entry
        })
    else:
        return render(request, "wiki/404.html")

def search_by_query(request):
    query = request.GET.get('q')
    if query:
        read_entry = util.get_entry(query)
        if read_entry:
            return render(request, "wiki/article.html", {
                "name": query.upper(),
                "read_entry": read_entry
            })

        matching_entries = [entry for entry in util.list_entries() if query.upper() in entry.upper()]
        if matching_entries:
            return render(request, "wiki/matching_entries.html", {
                "query": query,
                "matching_entries": matching_entries
            })

    return render(request, "wiki/404.html")

class ArticleForm(forms.Form):
    title = forms.CharField(label="Title",widget=forms.TextInput(attrs={"id": "title"}))
    content = forms.CharField(label="Content", widget=forms.Textarea)

    content.widget.attrs.update({"id": "content"})

def edit(request, name):
    return render(request, "wiki/edit.html", {
        "name": name,
        "read_entry": util.get_entry(name, False),
        "form": ArticleForm()
    })

def save(request, name):
    if request.method == "POST":
        content = request.POST.get("content")
        util.save_entry(name, content)
        return redirect(f'/wiki/{name}')

    return render(request, "wiki/404.html")
