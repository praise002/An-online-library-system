from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('<int:id>/', views.book_list, name='book_list'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('update_book/<int:pk>/', views.update_book, name='update_book'),
]