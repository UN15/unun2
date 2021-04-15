from django.shortcuts import render,get_object_or_404
from .models import Firstblog


def main(request):
    Firstblogs=Firstblog.objects.all()
    return render(request,'main.html',{'Firstblogs':Firstblogs})

def sub(request,id):
    b=get_object_or_404(Firstblog,pk=id)
    return render(request,'sub.html',{'b': b})