from rest_framework import viewsets
from rest_framework.response import Response
from .models import Task, TaskUser
from .serializers import TaskSerializer, UserSerializer
from rest_framework.decorators import action


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=["post"])
    def assign(self, request, pk=None):
        task = self.get_object()
        user_ids = request.data.get("user_ids", [])
        users = TaskUser.objects.filter(id__in=user_ids)
        task.assigned_users.set(users)
        return Response({"status": "task assigned"})


class UserViewSet(viewsets.ModelViewSet):
    queryset = TaskUser.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=["get"])
    def tasks(self, request, pk=None):
        user = self.get_object()
        tasks = user.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
