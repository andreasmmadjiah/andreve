from django.db import models
from django.utils import timezone

# Create your models here. Django default use primary key
class List_Blog(models.Model):
    title = models.CharField(max_length=80,unique=True)
    body = models.CharField(max_length=80,unique=True)
    date_created = models.DateTimeField('date created')

    def __str__(self):
        return self.title

class List_Creator(models.Model):
    id_blog = models.ForeignKey(List_Blog, on_delete=models.CASCADE) # delete all related key
    name = models.CharField(max_length=80)
    def __str__(self):
        return self.name


# class List_Creator(models.Model):
#     id_blog = models.ForeignKey(List_Blog, on_delete=models.CASCADE) # delete all related key
#     name = models.CharField(max_length=80)
#     def __str__(self):
#         return self.name