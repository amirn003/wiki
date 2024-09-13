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
