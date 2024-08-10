from django.urls import path

from . import views

urlpatterns = [
    path("getAllData/", views.getAllData, name="getAllDone"),
    path("getStatusData/", views.getStatusData, name="getStatusData"),
    path("addTask/", views.addTask, name="addTask"),
]