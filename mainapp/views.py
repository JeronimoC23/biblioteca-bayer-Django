from django.shortcuts import render, redirect
from blog.models import Event, Article, SubCom
from django.shortcuts import render, get_object_or_404



# Create your views here.
def index(request):
    events = Event.objects.filter(public=True)
    articles = Article.objects.filter(public=True)
    clase = "active"
    return render(request,'mainapp/index.html',{
        'title':'Home',
        'events':events,
        'articles': articles,
        'class':clase
    })

def aboutus(request):
    return render(request, 'mainapp/aboutus.html',{
        'title':'About'
    })

def subcom(request, subcom_id):
    subcomision = get_object_or_404(SubCom, id=subcom_id)
    articles = Article.objects.filter(subcomision=subcom_id)
    return render(request, 'subcomisiones/subcomision.html',{
        'subcomision': subcomision,
        'articles': articles
    })






