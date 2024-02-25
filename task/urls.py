from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

urlpatterns = [
    path('', views.taskViewSet, name='taskViewSet'),
]

router.register(r'addTask', views.addTaskViewSet, basename='addTask')
router.register(r'deleteTask', views.deleteTask, basename='deleteTask')
router.register(r'completedTask', views.completedTask, basename='completedTask')
router.register(r'editTask', views.editTask, basename='editTask')
router.register(r'undoCompletedTask', views.undoCompletedTask, basename='undoCompletedTask')

urlpatterns += router.urls