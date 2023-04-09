from django import forms
from . models import Category, Book, Review, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'description', 'image', 'category']