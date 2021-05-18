from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Book
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class Home(View):
    def get(self, request, *args, **kwargs):
        name = 'guest'
        context = {
            'name' : name ,
        }
        return render(request, 'library/home.html', context)



class Home2(TemplateView):
    template_name = 'library/home2.html'

    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['books'] = Book.objects.all()
        return context



class List_books(ListView):
    #-- address default : 'appname/modelname_list.html'
    #-- address default : 'library/book_list.html'
    template_name = 'library/list_books.html'
    model = Book
    ordering = ['-created']

    #-- set query set
    #queryset = Book.objects.filter(...)

    #-- set complex queryset
    #def get_queryset(self) :
    #   books = Book.objects.filter(...)
    #   return books

    #-- change object_list -to- allbooks in template file
    #context_object_name = 'allbooks'



class Detail_book(DetailView):
    #-- address default : 'library/book_detail.html'
    template_name = 'library/detail_book.html'
    model = Book
    context_object_name = 'book'


class Detail_Book_slug(DetailView):
    model = Book
    template_name = 'library/detail_book.html'
    slug_field = 'slug'
    slug_url_kwarg = 'myslug'

    def get_queryset(self, **kwargs) :
        if self.request.user.is_authenticated:
            return Book.objects.filter(slug = self.kwargs['myslug'])
        else :
            return Book.objects.none()

