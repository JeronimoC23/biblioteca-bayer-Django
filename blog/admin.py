from django.contrib import admin
from .models import Article, Event, SubCom,SubCom

from django.contrib.auth.models import *
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields= ('created_at','updated_at')
    search_fields = ('title', 'content','author')
    list_display = ('title', 'author','public', 'created_at')
    list_filter = ('public', 'author','subcomision')

   

class EventAdmin(admin.ModelAdmin):
    readonly_fields= ('created_at',)
    list_display = ('title', 'fecha', 'public','author')
    search_fields = ('title', 'description','fecha','author')

class SubCoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')



#Registro
admin.site.register(Event, EventAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(SubCom, SubCoAdmin)

#Quitar
admin.site.unregister(User)
admin.site.unregister(Group)

