from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from .models import Book, Comment
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, DetailView, FormView, CreateView, DeleteView, UpdateView, MonthArchiveView
from .forms import BookCommentsForm
from django.urls import reverse_lazy, reverse
from .forms import LibraryCreateForm

from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin





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



class Detail_Book_slug(LoginRequiredMixin, FormMixin, DetailView):
    model = Book
    template_name = 'library/detail_book.html'
    form_class = BookCommentsForm
    slug_field = 'slug'
    slug_url_kwarg = 'myslug'
    login_url = 'accounts:login'

    def get_success_url(self) :
        return reverse('library:detail_book_slug', kwargs={'myslug': self.the_book.slug} )

    def post(self, request, *args, **kwargs):
        self.the_book = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = Comment(book = self.the_book, name = form.cleaned_data['name'], body = form.cleaned_data['body'])
            comment.save()
        return super().form_valid(form)




"""
    def get_queryset(self, **kwargs) :
        if self.request.user.is_authenticated:
            return Book.objects.filter(slug = self.kwargs['myslug'])
        else :
            return Book.objects.none()
"""


class MonthBooks(MonthArchiveView):
    model = Book
    date_field = 'created'
    month_format = '%m'
    template_name = 'library/month_books.html'



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



class UpdateBook(UpdateView):
    model = Book
    fields = ('title',)
    template_name = 'library/update_book.html'
    success_url = reverse_lazy('library:list_books')





