from django.contrib import admin
from django.urls import path
from django.urls import include, path


from . import views

# app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add")
]
