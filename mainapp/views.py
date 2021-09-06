from django.shortcuts import render, redirect
from blog.models import Event, Article, SubCom
from django.shortcuts import render, get_object_or_404
from datetime import datetime



# Create your views here.
def index(request):
    today = datetime.today()
    events = Event.objects.filter(public=True, fecha__gte = today)
    articles = Article.objects.filter(public=True)
    subcoms = SubCom.objects.all()
    fav_articles = Article.objects.filter(fav=True, public=True)
    

    return render(request,'mainapp/index.html',{
        'title':'Home',
        'events':events,
        'articles': articles,
        'subcoms':subcoms,
        'fav_articles':fav_articles,

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

def feriadelibro(request):
    return render(request, 'mainapp/feria.html'
    )
def osvaldbayer(request):
    return render(request, 'mainapp/osvald.html'
    )






