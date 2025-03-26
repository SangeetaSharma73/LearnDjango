from django.urls import path
from .views import TaskCreateView, AssignTaskView, UserTasksView

urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='create-task'),
    path('tasks/<int:pk>/assign/', AssignTaskView.as_view(), name='assign-task'),
    path('users/<int:user_id>/tasks/', UserTasksView.as_view(), name='user-tasks'),
]
