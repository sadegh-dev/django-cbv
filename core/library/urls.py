from django.urls import path
from . import views


app_name = 'library'

urlpatterns = [
    path('view-class/', views.Home.as_view())
]
