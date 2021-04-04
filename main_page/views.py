from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import List_Blog
from django.views import generic
from django.contrib.auth.models import User

from django.contrib import auth

# Create your views here.
# remember you are using generic, you need to only defined, model , template_name, or context_object_name
def home(request):
    context = List_Blog.objects.all()

    return render(request,'main_page/index.html',{'all':context})

def login_user(request):
    if request.POST.get('action')=='post':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'is_ok':'0'})
        else:
            # User.objects.create_user(username=username,password=password)
            return JsonResponse({'is_ok':'1'})
    return render(request,'main_page/login.html')


# coba2
# def home(request):
#     context = List_Blog.objects.all()
#     all_context = {}
#     all_context['list_blog'] = context
    # print(context)
    
    # return HttpResponse("You don't have a favorite color.")
    
#     if "session_id" not in request.session:
#         request.session['session_id'] = 1
#     else:
#         request.session['session_id'] += 1
#         if request.session['session_id'] >3:
#             print("Will delete")
#             del request.session['session_id']
#     print("Cookies")
#     print(request.session.keys())
#     print(request.session.items())
#     print(request.COOKIES)

# #     user = User.objects.create_user(username='john',
# # ...                                 email='jlennon@beatles.com',
# # ...                                 password='glass onion')
##      user.save()
#     user = auth.authenticate(username="andreve",password="password")

#     # user.is_staff = True
#     if user.is_authenticated:
#         auth.login(request,user)
#         all_context['username'] = user.username
#         print(request.user.username)
#         print(request.user.is_superuser)
#         auth.logout(request)
#     print(request.user.is_anonymous)
    # for field in User._meta.fields:
    #     print(field.name)
    # print(User.objects.filter(username=user))
    
    # print(request.session.set_test_cookie())
    # print(request.session.test_cookie_worked())
    # print(request.session.delete_test_cookie())

    
    
    
    # print("Session")
    # print(request.session.keys())

    # return render(request,'main_page/index.html',all_context)
    # return render(request,'main_page/index.html',{'all':context})