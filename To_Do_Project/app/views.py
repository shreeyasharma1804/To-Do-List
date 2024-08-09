from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import UserTasks

def home(request):
    pass

def getToDo(request):
    print(request)
    data = UserTasks.objects.all()
    JSONData = {
        "Data": list(data.values())
    }
    return JsonResponse(JSONData)

def getDone(request):
    return JsonResponse({'Task1_User1': {'Task': 'Task1', 'User': 'User1', 'Time': 'Time', 'Status': 'Done'}})

def addTask(request):
    pass

def deleteTask(request):
    pass


