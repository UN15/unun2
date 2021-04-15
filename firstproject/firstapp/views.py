from django.shortcuts import render

def start(request):
    return render(request,"start.html")

def result(request):
    name=request.GET['username']
    return render(request,"result.html",{'inputname': name})
