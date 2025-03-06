import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Project (models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date_publishied")
    def __str__(self):
        return self.name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Task (models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    priority = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.text