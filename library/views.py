from django.shortcuts import render, get_object_or_404
from . models import Book, Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'library/category/list/category.html', {'categories': categories})


def book_list(request, id):
    category = Category.objects.get(id=id)
    books = category.book_set.filter()
    context = {'category': category, 'books': books}
    return render(request, 'library/category/list/book.html', context)

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    context = {'book': book}
    return render(request, 'library/category/list/detail.html', context)