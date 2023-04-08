from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    bio = models.TextField(null=True, blank=True)
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', default='users/default.jpg')
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)
    
class Review(models.Model):
    rating = models.IntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_review')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_review')

# class Loan(models.Model):
#     due_date = models.DateTimeField()
#     date_returned = models.DateTimeField()
#     user = models
#     book = models.