from django.shortcuts import render
from rest_framework import viewsets, status
from .models import tasks
from .serializers import taskSerializer
from rest_framework.response import Response
 
# Create your views here.

def taskViewSet(request):
    return render(request, 'todo.html')
    

class addTaskViewSet(viewsets.ViewSet):
    def create(self, request):
        print("111")
        task = request.data.get('task')
        print(task)
        new_data = {
            'description':task
        }    
        serializer = taskSerializer(data=new_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_200_OK)
        
class deleteTask(viewsets.ViewSet):
    def create(self,request):
        taskId = request.data.get('taskId')
        try:
            task_instance = tasks.objects.get(taskId=taskId)
        except tasks.DoesNotExist:
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        task_instance.status = 2 
        task_instance.save()

        serializer = taskSerializer(task_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class completedTask(viewsets.ViewSet):
    def create(self,request):
        taskId = request.data.get('taskId')
        try:
            task_instance = tasks.objects.get(taskId=taskId)
        except tasks.DoesNotExist: 
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        task_instance.status = 1
        task_instance.save()

        serializer = taskSerializer(task_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)    

class editTask(viewsets.ViewSet):
    def create(self,request):
        taskId = request.data.get('taskId')
        description = request.data.get('content')

        try:
            task_instance = tasks.objects.get(taskId=taskId)
        except tasks.DoesNotExist:
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        # task_instance.description = description
        # task_instance.save()

        # serializer = taskSerializer(task_instance)
        # return Response(serializer.data, status=status.HTTP_200_OK) 

        # Update task instance with new data using serializer
        serializer = taskSerializer(task_instance, data={'description': description}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class undoCompletedTask(viewsets.ViewSet):
    def create(self,request):
        taskId = request.data.get('taskId')
        try:
            task_instance = tasks.objects.get(taskId = taskId)
        except tasks.DoesNotExist:
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        task_instance.status = 0
        task_instance.save()

        serializer = taskSerializer(task_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)                   

