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
        new_data = {
            'description':task
        }    
        serializer = taskSerializer(data=new_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_200_OK)