from django.conf.urls import include

from django.urls import path

from . import views

urlpatterns = [

    path('', views.allBlogs, name='stories'),
    path('<int:pk>/',views.BlogDetail.as_view(), name='detail'),
] 
