from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer, TaskAssignmentSerializer

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class AssignTaskView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskAssignmentSerializer
    permission_classes = [IsAuthenticated]

class UserTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Task.objects.filter(assigned_users__id=user_id)
