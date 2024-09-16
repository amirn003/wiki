from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from encyclopedia import util


def index(request):
    return HttpResponse("Wiki Index!")

def search_by_title(request, name):
    if util.get_entry(name):
        read_entry = util.get_entry(name)
        return HttpResponse(f"<h1> {name} </h1><br> <p> {read_entry} </p>")
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
                print(f"{query.upper()} ===> {entry}")
                matching_entries.append(entry)

        return HttpResponse(f"<h1> {query} </h1><br> <p> {matching_entries} </p>")


        #return HttpResponseNotFound("Page not found.")
