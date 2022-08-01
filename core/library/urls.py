from django.urls import path
from . import views


app_name = 'library'

urlpatterns = [
    path('view-class/', views.Home.as_view()),
    path('template-class/', views.Hometemp.as_view()),
    path('redirect-class/<str:name>/', views.HomeRedir.as_view()),
]
