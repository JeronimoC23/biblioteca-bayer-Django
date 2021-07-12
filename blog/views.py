from mainapp.views import subcom
from django.shortcuts import render, get_object_or_404
from blog.models import Article,  Event, SubCom
from django.core.paginator import Paginator



# Create your views here.

def list(request):
    #sacar articulos
    articles = Article.objects.all()
    #paginar articulos
    paginator = Paginator(articles, 4)
    #recoger numero de pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    
    return render(request, "articles/list.html",{
        'title':'Articles',
        'articles': page_articles,
    })



def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    return render (request, 'articles/detail.html',{
        "article": article,
    })

def event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    return render (request, './mainapp/templates/mainapp/index.html',{
        "event": event,
        })

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    return render (request, 'events/detail_event.html',{
        "event": event,
    })
