from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone


# Create your views here.


def main(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/main.html', {'blogs' :blogs})

def write(request):
    return render(request, 'blog/write.html')

def create(request):
    write_blog = Blog()
    write_blog.title = request.POST['title']
    write_blog.writer = request.POST['writer']
    write_blog.body = request.POST['body']
    write_blog.pub_date = timezone.now()
    write_blog.save()
    return redirect ('main')

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'blog/detail.html', {'blog' : blog})

def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'blog/edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id = id)
    delete_blog.delete()
    return redirect('main')