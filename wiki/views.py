from django.shortcuts import render
from django.http import HttpResponse
from encyclopedia import util


def search_by_title(request, name):
    read_entry = util.get_entry(name)
    return HttpResponse(f"<h1> {name} </h1><br> <p> {read_entry} </p>")
