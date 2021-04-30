from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blogupdate

def mainpage(request):
    blogupdates = Blogupdate.objects.all()
    return render(request, 'mainpage.html', {'blogupdates': blogupdates})

def subpage(request, id):
   subpages = get_object_or_404(Blogupdate, pk = id)
   return render(request, 'subpage.html', {'subpages': subpages})

def newpage(request):
    return render(request, 'newpage.html')

def create(request):
    new = Blogupdate()
    new.title = request.POST['new_title']
    new.writer = request.POST['new_writer']
    new.body = request.POST['new_body']
    new.pub_date = timezone.now()
    new.save()
    return redirect('subpage', new.id)

def edit(request, id):
    eblog = Blogupdate.objects.get(id = id)
    return render(request, 'e_blog.html', {'eblog': eblog})

def update(request, id):
    ublog = Blogupdate.objects.get(id = id)
    ublog.title = request.POST['new_title']
    ublog.writer = request.POST['new_writer']
    ublog.body = request.POST['new_body']
    ublog.pub_date = timezone.now()
    ublog.save()
    return redirect('subpage', ublog.id)

def delete(request, id):
    dblog = Blogupdate.objects.get(id = id)
    dblog.delete()
    return redirect('mainpage')