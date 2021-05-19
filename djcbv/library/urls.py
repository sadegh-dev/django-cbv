from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('h/', views.Home2.as_view(), name='home2'),
    path('list-books/', views.List_books.as_view(), name='list_books'),
    path('detail-book/<int:pk>/', views.Detail_book.as_view(), name='detail_book'),
    path('detail-book/<slug:myslug>/', views.Detail_Book_slug.as_view(), name='detail_book_slug'),
    path('create/', views.LibraryCreate.as_view(), name='create_books'),
    path('create2/', views.LibraryCraete2.as_view(), name='create_books2'),
]




