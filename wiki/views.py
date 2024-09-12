from django.shortcuts import render
from django.http import HttpResponse


def search_by_title(request, name):
    return HttpResponse(f"This is the title searched: {name}")
