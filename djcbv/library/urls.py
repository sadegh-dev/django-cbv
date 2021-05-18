from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('h', views.Home2.as_view(), name='home2'),
]