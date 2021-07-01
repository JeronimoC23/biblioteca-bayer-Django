from django.urls import path
from . import views 

urlpatterns = [
    path('articles/', views.list, name="list"),
    path('category/<int:category_id>', views.category, name="category"),
    path('article/<int:article_id>', views.article, name="article")
]