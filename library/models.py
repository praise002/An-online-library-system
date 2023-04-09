from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', default='users/default.jpg')
    category = models.ManyToManyField(Category)
    
    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['title'])
        ]
        
    def __str__(self):
        return self.title
    
class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    bio = models.TextField(null=True, blank=True)
    book = models.ManyToManyField(Book)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        
    def __str__(self):
        return self.name
    
    
class Review(models.Model):
    rating = models.IntegerField(null=True, blank=True, 
                                validators=[
                                    MinValueValidator(limit_value=1),
                                    MaxValueValidator(limit_value=100)
                                    ])
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_review')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_review')

    def __str__(self):
        # return str(self.rating)
        return f'{self.user} {self.book} {self.rating}'
    
# class Loan(models.Model):
#     due_date = models.DateTimeField()
#     date_returned = models.DateTimeField()
#     user = models
#     book = models.

class Tag(models.Model):
    pass