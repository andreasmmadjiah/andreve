from . import views
from django.urls import path

app_name = 'main_page'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login_user'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]