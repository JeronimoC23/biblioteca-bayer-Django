from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category, Event
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

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(categories=category_id)
    return render(request, 'categories/category.html',{
        'category': category,
        'articles': articles
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