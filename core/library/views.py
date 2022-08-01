from django.shortcuts import render
from django.views import View

class Home(View):

    http_method_names= ['get', 'options']

    def get(self, request):
        return render(request, 'home.html')
    
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