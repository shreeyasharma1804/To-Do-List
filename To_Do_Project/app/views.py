from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import UserTasks

def getAllData(request):
    username = request.GET.get('username', None)
    if(username):
        data = UserTasks.objects.filter(username = username)
        JSONData = {
            "Data": list(data.values())
        }
        return JsonResponse(JSONData)

def getStatusData(request):
    username = request.GET.get('username', None)
    status = request.GET.get('status', None)
    data = UserTasks.objects.filter(username=username, status=status)
    JSONData = {
        "Data": list(data.values())
    }
    return JsonResponse(JSONData)


def addTask(request):
    if(request.method == "POST"):
        print(request.body)
    return HttpResponse("Added")

def deleteTask(request):
    pass

def modifyTask(request):
    pass


