from django.urls import path

from . import views

urlpatterns = [
    #new_url = root url + {the first argument in path(route)}
    path("", views.index, name="index"),
]