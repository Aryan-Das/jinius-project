from django import http
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from .models import Blog, Comment
from django.views import View
# Create your views here.
def allBlogs(request):
   
    blogs = Blog.objects.all().order_by('pub_date').reverse()
    length = len(blogs)
    return render(request,'blog/allBlogs.html',{'blogs':blogs})




class BlogDetail(View):
    def get(self,request,pk,*args,**kwargs):
        blog = Blog.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.all().filter(blog = blog).order_by('pub_date').reverse()
        context = {
            'blog': blog,
            'form': form,
            'comments': comments,
        }
        return render(request,'blog/detail.html',context)
    def post(self,request,pk,*args,**kwargs):
        blog = Blog.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('/stories/' + str(pk))
        comments = Comment.objects.all().filter(blog = blog).order_by('pub_date').reverse()
        context = {
            'blog': blog,
            'form': form,
            'comments': comments,
        }
        return render(request,'blog/detail.html', context)     
            

