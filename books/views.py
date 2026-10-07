from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Author, Book, Genre


def book_list(request):
  """Список доступных книг + доп. данные в контексте."""
  books = Book.objects.filter(is_available=True).select_related('author')
  total_count = books.count()
  has_books = books.exists()

  context = {
      'title': 'Каталог книг',
      'total_count': total_count,
      'has_books': has_books,
      'books': books,
  }
  return render(request, 'books/book_list.html', context)


def book_detail(request, slug):
  """Детальная страница книги с обработкой 404 и оптимизацией."""
  book = get_object_or_404(
      Book.objects.select_related('author').prefetch_related('genres'),
      slug=slug,
      is_available=True,
  )

  context = {
      'title': book.title,
      'back_url': reverse('books:book_list'), 
      'book': book,
  }
  return render(request, 'books/book_detail.html', context)


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'books/author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.books.filter(is_available=True)
    return render(request, 'books/author_detail.html', {'author': author, 'books': books})

def about_view(request):
    return render(request, 'books/about.html', {'title': 'О библиотеке'})

