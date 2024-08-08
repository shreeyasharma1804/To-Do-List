from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def getToDo(request):
    return JsonResponse({'Task1_User1': {'Task': 'Task1', 'User': 'User1', 'Time': 'Time', 'Status': 'To Do'}})

def getDone(request):
    return JsonResponse({'Task1_User1': {'Task': 'Task1', 'User': 'User1', 'Time': 'Time', 'Status': 'Done'}})
