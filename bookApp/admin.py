from django.contrib import admin

from .models import Book, Hero

class HeroInline(admin.StackedInline):
    model = Hero
    extra = 2

class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'pub_date']
    list_filter = ['title']
    search_fields = ['title']
    list_per_page = 10
    fieldsets = [('基础信息', {'fields': ['title']}),
                 ('详细信息', {'fields': ['pub_date']}), ]
    inlines = [HeroInline]
class HeroAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sex', 'content']
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 10
    fieldsets = [('基础信息', {'fields': ['name','gender']}),
                 ('详细信息', {'fields': ['content']}), ]

admin.site.register(Book, BookAdmin)
admin.site.register(Hero, HeroAdmin)
