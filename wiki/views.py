from django.shortcuts import render, redirect
from django.http import HttpResponse
from encyclopedia import util


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
    if query and util.get_entry(query) and query is not None:
        read_entry = util.get_entry(query)
        # return HttpResponse(f"<h1> {query} </h1><br> <p> {read_entry} </p>")
        return render(request, "wiki/article.html", {
            "name": query.upper(),
            "read_entry": read_entry
        })
    else:
        entries = util.list_entries()
        matching_entries = []
        for entry in entries:
            if query.upper() in entry.upper():
                matching_entries.append(entry)

        if matching_entries:
            #return HttpResponse(f"<h1> Articles found for your search: {query} </h1><br> <p> {matching_entries} </p>")
            return render(request, "wiki/matching_entries.html", {
                "query": query,
                "matching_entries": matching_entries
            })

    return render(request, "wiki/404.html")


def edit(request, name):
    return render(request, "wiki/edit.html", {
        "name": name,
        "read_entry": util.get_entry(name, False)
    })

def save(request, name):
    if request.method == "POST":
        content = request.POST.get("content")
        util.save_entry(name, content)
        # return HttpResponse(f"<h1> Article '{name}' saved! </h1>")
        return redirect(f'/wiki/{name}')

    return render(request, "wiki/404.html")
