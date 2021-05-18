from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Book

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



