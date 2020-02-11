from django.contrib import admin
from .models import Author, Category, Artical

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['__str__', 'details']
    class Meta:
        model = Author
admin.site.register(Author, AuthorAdmin)

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'active', 'updated']
    list_editable = ['active']
    list_filter = ['active', 'timestamp']
    readonly_fields = ['timestamp', 'updated']
    list_per_page = 10
    class Meta:
        model = Category
admin.site.register(Category, CategoryAdmin)

class ArticalAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body']
    list_display = ['title', 'artical_author', 'category', 'active', 'updated']
    list_editable = ['active']
    list_filter = ['category', 'active', 'timestamp']
    readonly_fields = ['timestamp', 'updated']
    list_per_page = 10
    class Meta:
        model = Artical
admin.site.register(Artical, ArticalAdmin)
