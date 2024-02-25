from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

urlpatterns = [
    path('', views.taskViewSet, name='taskViewSet'),
]

router.register(r'addTask', views.addTaskViewSet, basename='addTask')

urlpatterns += router.urls