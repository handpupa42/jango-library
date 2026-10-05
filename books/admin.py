from django.contrib import admin
from django.db.models import Count
from .models import Author, Genre, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date')
    search_fields = ('first_name', 'last_name')
    list_filter = ('birth_date',)
    ordering = ('last_name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'book_count')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(_book_count=Count('books'))

    @admin.display(description='Количество книг', ordering='_book_count')
    def book_count(self, obj):
        return obj._book_count

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'price', 'is_available')
    list_editable = ('price', 'is_available')
    search_fields = ('title', 'description')
    list_filter = ('is_available', 'author', 'genres')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    list_select_related = ('author',)
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'slug', 'description')
        }),
        ('Автор и жанры', {
            'fields': ('author', 'genres')
        }),
        ('Издание', {
            'fields': ('year',)
        }),
        ('Цена и наличие', {
            'fields': ('price', 'is_available')
        }),
        ('Служебное', {
            'classes': ('collapse',),  
            'fields': ('created_at', 'updated_at'),
        }),
    )
