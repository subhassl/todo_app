from django.shortcuts import render
from . import models
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Task


def dummyview(request):

    tasks = models.Task.objects.all()
    for task in tasks:
        task_dict = {
            'title': task.title,
            'description': task.description 
        }
        print(task_dict)

    print(tasks)


    task_dicts = models.Task.objects.all().values("title","user")
    print(task_dicts)

    return render(request=request, template_name='base/task_detail.html')

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    