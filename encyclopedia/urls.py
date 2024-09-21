from django.contrib import admin
from django.urls import path
from django.urls import include, path

from . import views

# app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("add/new_entry/", views.new_entry, name="new_entry")
    # path('entries/<str:title>', views.new_entry, name = "article_path")

]
