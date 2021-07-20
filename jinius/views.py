from django.shortcuts import render
from blog.models import Blog

def home(request):
    blogs = Blog.objects.all().order_by('pub_date').reverse()[:2]
    length = len(blogs)
    return render(request, 'home.html',{'blogs':blogs,'length':length})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


