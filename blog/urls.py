from django.conf.urls import include

from django.urls import path

from . import views

urlpatterns = [

    path('', views.allBlogs, name='stories'),
    path('<int:blog_id>/',views.detail, name='detail'),
] 
