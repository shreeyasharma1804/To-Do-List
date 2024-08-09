from django.db import models

class UserTasks(models.Model):
    username = models.CharField(max_length=50)
    taskname = models.CharField(max_length=50)
    status = models.CharField(max_length=50)