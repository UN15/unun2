from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Finalblog2
from .forms import BlogForm

def blogmain2(request):
    obj2 = Finalblog2.objects.all()
    return render(request, 'blogmain2.html', {'obj2': obj2})

def blogsub2(request, id):
    sub2id= get_object_or_404(Finalblog2, pk = id)
    return render(request, 'blogsub2.html', {'sub2id': sub2id})

def blognew2(request):
    b_form = BlogForm()
    return render(request, 'blognew2.html',{'b_form': b_form})

def create2(request):
    b_form = BlogForm(request.POST, request.FILES)
    if b_form.is_valid():
        n2blog = b_form.save(commit=False)
        n2blog.pub_date = timezone.now()
        n2blog.save()
        return redirect('blogsub2', n2blog.id)
    return redirect('blogmain2')

def edit2(request, id):
    e2blog = Finalblog2.objects.get(id = id)
    return render(request, 'blogedit2.html', {'e2blog': e2blog})

def update2(request, id):
    u2blog = Finalblog2.objects.get(id = id)
    u2blog.title = request.POST['new2title']
    u2blog.writer = request.POST['new2writer']
    u2blog.body = request.POST['new2body']
    u2blog.pub_date = timezone.now()
    u2blog.save()
    return redirect('blogsub2', u2blog.id)

def delete2(request, id):
    d2blog = Finalblog2.objects.get(id = id)
    d2blog.delete()
    return redirect('blogmain2')

