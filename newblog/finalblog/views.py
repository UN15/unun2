from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Finalblog

def blogmain(request):
    blogobj = Finalblog.objects.all()
    return render(request, 'blogmain.html', {'blogobj': blogobj})

def blogsub(request, id):
    blogid= get_object_or_404(Finalblog, pk = id)
    return render(request, 'blogsub.html', {'blogid': blogid})

def blognew(request):
    return render(request, 'blognew.html')

def create(request):
    newpage = Finalblog()
    newpage.title = request.POST['n_title']
    newpage.writer = request.POST['n_writer']
    newpage.body = request.POST['n_body']
    newpage.pub_date = timezone.now()
    newpage.save()
    return redirect('blogsub', newpage.id)

def edit(request, id):
    blog_edit = Finalblog.objects.get(id = id)
    return render(request, 'blogedit.html', {'blog_edit': blog_edit})

def update(request, id):
    blog_update = Finalblog.objects.get(id = id)
    blog_update.title = request.POST['n_title']
    blog_update.writer = request.POST['n_writer']
    blog_update.body = request.POST['n_body']
    blog_update.pub_date = timezone.now()
    blog_update.save()
    return redirect('blogsub', blog_update.id)

def delete(request, id):
    blog_delete = Finalblog.objects.get(id = id)
    blog_delete.delete()
    return redirect('blogmain')
