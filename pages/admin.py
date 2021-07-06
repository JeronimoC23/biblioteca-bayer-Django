from django.contrib import admin
from .models import Page
# Register your models here.
#configuracion extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('public',)
    list_display = ('title', 'public', 'created_at')
    ordering = ('created_at',)


admin.site.register(Page, PageAdmin)

