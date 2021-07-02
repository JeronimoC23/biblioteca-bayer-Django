from django.shortcuts import render, redirect



# Create your views here.

def index(request):
    return render(request,'mainapp/index.html',{
        'title':'Home'
    })

def aboutus(request):
    return render(request, 'mainapp/aboutus.html',{
        'title':'About'
    })

