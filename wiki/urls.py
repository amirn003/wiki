"""wiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'wiki'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("encyclopedia.urls"), name="encyclopedia_index"),
    # path('wiki/', views.index, name="wiki_index"),
    path('wiki/', views.search_by_query, name="search_by_query"),
    path('wiki/<str:name>/', views.search_by_title, name="search_by_title"),
    path('wiki/edit', views.edit, name="edit")

    #path('', views.index, name="wiki_index"),
    #path('<str:name>/', views.search_by_title, name="search_by_title")
]
