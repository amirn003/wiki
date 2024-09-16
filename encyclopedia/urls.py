from django.contrib import admin
from django.urls import path
from django.urls import include, path


from . import views

# app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index")

    # path('admin/', admin.site.urls),
    # path('', include("encyclopedia.urls"), name="encyclopedia_index"),
    # path('wiki/', include('wiki.urls'), name="wiki")
]
