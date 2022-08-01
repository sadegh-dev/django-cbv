# views

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

# html

<h1>home </h1>
{{ request.method }}


# urls


from django.urls import path
from . import views



urlpatterns = [
    path('85/', views.Home.as_view())
]