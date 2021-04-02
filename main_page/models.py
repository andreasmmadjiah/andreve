from django.db import models
from django.utils import timezone

# Create your models here. Django default use primary key
class List_Menu(models.Model):
    column = models.CharField(max_length=80,unique=True)
    apps = models.CharField(max_length=80,unique=True)
    date_created = models.DateTimeField('date created')

    def __str__(self):
        return self.column