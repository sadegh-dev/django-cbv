from django.urls import path
from . import views


app_name = 'library'

urlpatterns = [
    path('view-class/<str:name>/', views.Home.as_view(), name = 'home'),
    path('template-class/', views.Hometemp.as_view()),
    path('redirect-class/<str:name>/', views.HomeRedir.as_view()),
    path('list-books/', views.ListBooks.as_view()),
    path('detail/<str:name>/', views.DetailView.as_view(), name='detail-book'),

]
