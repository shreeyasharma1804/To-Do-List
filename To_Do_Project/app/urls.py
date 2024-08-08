from django.urls import path

from . import views

urlpatterns = [
    path("getToDo/", views.getToDo, name="getToDo"),
    path("getDone/", views.getDone, name="getDone"),
]