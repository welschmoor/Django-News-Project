from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'category', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    # edit right in the column:
    list_editable = ('is_published',)
    # this creates a filter winow
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',) #don't forget the tuple comma

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
