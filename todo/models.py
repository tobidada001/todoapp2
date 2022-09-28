from django.db import models

class Task(models.Model):
    
    task_name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, default = 'Pending')
    task_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.task_name


# Create your models here.
