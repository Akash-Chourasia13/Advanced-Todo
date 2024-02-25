from django.db import models

# Create your models here.
class tasks(models.Model):
    taskId = models.AutoField(primary_key=True)
    description = models.TextField()
    STATUS_CHOICES = {
        '0':'incomplete',
        '1':'completed',
        '2':'deleted'
    }
    status = models.IntegerField(choices=STATUS_CHOICES,default='0')
    createdDate = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True)

    def __str__(self):
        return self.taskId
