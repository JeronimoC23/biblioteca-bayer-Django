from django.shortcuts import render, redirect
from blog.models import Event, Article



# Create your views here.

def index(request):
    events = Event.objects.all()
    articles = Article.objects.filter(public=True)
    return render(request,'mainapp/index.html',{
        'title':'Home',
        'events':events,
        'articles': articles
    })

def aboutus(request):
    return render(request, 'mainapp/aboutus.html',{
        'title':'About'
    })

