from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from encyclopedia import util


def index(request):
    return HttpResponse("Wiki Index!")

def search_by_title(request, name):
    if util.get_entry(name):
        read_entry = util.get_entry(name)
        # return HttpResponse(f"<h1> {name} </h1><br> <p> {read_entry} </p>")

        # return render(request, "wiki/article.html")
        return render(request, "wiki/article.html", {
            "name": name,
            "read_entry": read_entry
        })
    else:
        return HttpResponseNotFound("Page not found.")

def search_by_query(request):
    query = request.GET.get('q')
    if query and util.get_entry(query):
        read_entry = util.get_entry(query)
        return HttpResponse(f"<h1> {query} </h1><br> <p> {read_entry} </p>")
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
        else:
            return HttpResponseNotFound("Page not found.")


def edit(request):
    return render(request, "wiki/edit.html")
