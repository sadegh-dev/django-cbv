from django.shortcuts import render
from django.views import View

class Home(View):

    http_method_names= ['get', 'options']
    
    def setup(self, request, *args, **kwargs) :
        self.name = kwargs.get('name') # send by URL
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {
            'admin':'False' ,
            'name' : self.name
            }
        return render(request, 'home.html', context)
    
    def options(self, request, *args, **kwargs):
        response = super().options(request, *args, **kwargs)
        response.headers['host'] = 'localhost'
        response.headers['user'] = request.user
        return response
    
    def http_method_not_allowed(self, request, *args, **kwargs) :
        super().http_method_not_allowed(request, *args, **kwargs)
        return render(request, 'http_method_not_allowed.html')


######################################

from django.views.generic import TemplateView
from .models import Book

class Hometemp(TemplateView):
    template_name = 'hometemp.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context


######################################

from django.views.generic import RedirectView

class HomeRedir(RedirectView):
    #url = '/home/add/'
    #OR
    #url = 'https://google.com'
    #OR
    pattern_name = 'library:home'

    # http : ......./?name=harry
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        print(kwargs.get('name'))
        return super().get_redirect_url(*args, **kwargs)


######################################

from django.views.generic.list import ListView
from .models import Book

class ListBooks(ListView):
    template_name = 'list_books.html'
    context_object_name= 'books'
    ordering = '-date_publish'

    def get_queryset(self):
        result = Book.objects.filter(pages__gt = 200)
        return result
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop'] = 'book-center'
        return context


##########################################

from django.views.generic.detail import DetailView
from .models import Book

class BookDetail(DetailView):
    template_name = 'detail_book.html'

    def get_object(self, queryset=None):
        return Book.objects.get (name = self.kwargs['name'])

