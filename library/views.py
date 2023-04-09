from django.shortcuts import render, get_object_or_404, redirect
from . models import Book, Category
from . forms import BookForm

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

def add_book(request):
    if request.method == 'POST':
        form = BookForm(data=request.POST, files=request.FILES)  #its a dict
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()
        
    context = {'form': form}
    return render(request, 'library/book/book_form.html', context)

def update_book(request, pk):
    book = Book.objects.get(id=pk)
    
    if request.method == 'POST':
        form = BookForm(data=request.POST, files=request.FILES, instance=book)  #its a dict
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm(instance=book)
        
    context = {'form': form}
    return render(request, 'library/book/book_form.html', context)
