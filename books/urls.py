from django.urls import path

from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path('<uuid:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('task/<uuid:pk>', TaskUpdateView.as_view(), name= 'edit_task'),
]
