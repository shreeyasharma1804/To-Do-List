from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import UserTasks
from django.views.decorators.csrf import csrf_exempt
import json

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

@csrf_exempt
def addTask(request):
    if(request.method == "POST"):
        data = json.loads(request.body)
        username = data.get('username', None)
        taskname = data.get('taskname', None)
        status = data.get('status', None)
        newEntry = UserTasks(username=username, taskname=taskname, status=status)
        newEntry.save()
    return HttpResponse("Added")

@csrf_exempt
def deleteTask(request):
    if(request.method == "POST"):
        data = json.loads(request.body)
        username = data.get('username', None)
        taskname = data.get('taskname', None)
        status = data.get('status', None)
        UserTasks.objects.filter(username=username, taskname=taskname, status=status).delete()
    return HttpResponse("Deleted")    

@csrf_exempt
def modifyStatus(request):
    if(request.method == "POST"):
        data = json.loads(request.body)
        username = data.get('username', None)
        taskname = data.get('taskname', None)
        status = data.get('status', None)
        task = UserTasks.objects.get(username=username, taskname=taskname)
        if(status is not None):
            task.status = status
        task.save()          
    return HttpResponse("Status changed")


