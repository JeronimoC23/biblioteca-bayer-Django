from blog.models import Article, SubCom, Event

def get_articles(request):

    articles = Article.objects.filter(public=True).values_list('id', 'title', 'slug','image','author')
    
    return {
        'articles': articles
    }

def get_subcomisiones(request):
    subcomisiones_in_use = Article.objects.filter(public=True).values_list('subcomision', flat=True)
    subcomisiones = SubCom.objects.filter(id__in=subcomisiones_in_use).values_list('id', 'name','description','image')
    
    return {
        'subcomisiones': subcomisiones,
        'ids':subcomisiones_in_use

    }

