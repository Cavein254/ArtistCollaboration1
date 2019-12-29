from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Task


# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/task_detail.html'
    context_object_name = 'task_detail'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task/create_task.html'
    fields = ['profession_required', 'task_title', 'task_description', 'expiry_date']


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task/edit_task.html'
    fields = ['profession_required', 'task_title', 'task_description', 'expiry_date']

