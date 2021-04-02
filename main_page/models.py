from django.db import models
from django.utils import timezone

# Create your models here. Django default use primary key
class List_Blog(models.Model):
    title = models.CharField(max_length=80,unique=True)
    body = models.CharField(max_length=80,unique=True)
    date_created = models.DateTimeField('date created')

    def __str__(self):
        return self.title