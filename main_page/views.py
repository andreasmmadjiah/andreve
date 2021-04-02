from django.shortcuts import render
from .models import List_Blog
from django.views import generic


# Create your views here.
# remember you are using generic, you need to only defined, model , template_name, or context_object_name
def home(request):
    context = List_Blog.objects.all()

    return render(request,'main_page/index.html',{'all':context})
    
