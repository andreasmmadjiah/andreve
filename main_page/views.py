from django.shortcuts import render
from .models import List_Menu
from django.views import generic


# Create your views here.
# remember you are using generic, you need to only defined, model , template_name, or context_object_name
class Show_Menu(generic.ListView):
    
