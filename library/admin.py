from django.contrib import admin
from . models import Book, Category, Review, Author 

# admin.register(Cattegory)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'description']

# admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ['rating', 'email', 'description', 'image', 'category']

# admin.register(Author)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'bio', 'book']
    
# admin.register(Review)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ['rating', 'comment', 'created', 'updated', 'user', 'book']

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Author)