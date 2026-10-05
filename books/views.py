from django.shortcuts import get_object_or_404, render
from .models import Author, Book

def book_list(request):
    books = Book.objects.filter(is_available=True).select_related('author')
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, slug):
    book = get_object_or_404(
        Book.objects.select_related('author').prefetch_related('genres'), slug=slug
    )
    return render(request, 'books/book_detail.html', {'book': book})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'books/author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.books.filter(is_available=True)
    return render(request, 'books/author_detail.html', {'author': author, 'books': books})

def about_view(request):
    return render(request, 'books/about.html', {'title': 'О библиотеке'})
