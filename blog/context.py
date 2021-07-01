from blog.models import Article, Category

def get_articles(request):

    articles = Article.objects.filter(public=True).values_list('id', 'title', 'slug','image','user')
    
    return {
        'articles': articles
    }

def get_categories(request):
    categories_in_use = Article.objects.filter(public=True).values_list('categories', flat=True)
    categories = Category.objects.filter(id__in=categories_in_use).values_list('id', 'name')
    
    return {
        'categories': categories,
        'ids':categories_in_use

    }