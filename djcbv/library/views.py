from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Book
from django.views.generic import ListView, DetailView, FormView, CreateView, DeleteView 

from .forms import LibraryCreateForm
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib import messages




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



class LibraryCreate(FormView):
    form_class = LibraryCreateForm
    template_name = 'library/library_create.html'
    success_url = reverse_lazy('library:list_books')

    def form_valid(self, form):
        self.create_book(form.cleaned_data)
        return super().form_valid(form)

    def create_book(self, data):
        book = Book(title=data['title'], slug=slugify(data['title']))
        book.save()
        messages.success(self.request, 'your book added', 'success')



class LibraryCraete2(CreateView):
    model = Book
    fields=('title',)
    template_name = 'library/library_create2.html'
    success_url = reverse_lazy('library:list_books')

    def form_valid(self, form):
        book = form.save(commit=False)
        book.slug = slugify(form.cleaned_data['title'])
        book.save()
        messages.success(self.request, 'your book added2', 'success')
        return super().form_valid(form)



class DeleteBook(DeleteView):
    model = Book
    template_name = 'library/delete_book.html'
    success_url = reverse_lazy('library:list_books')




