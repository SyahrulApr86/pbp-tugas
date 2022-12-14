from django.db import models
import datetime

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title