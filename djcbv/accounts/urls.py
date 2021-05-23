from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('reset/', views.UserPassReset.as_view(), name='reset_pass'),
    path('reset/done/', views.UserPassResetDone.as_view(), name='reset_pass_done'),
    path('reset/<uidb64>/<token>', views.UserPassResetConfirm.as_view(), name='reset_pass_confirm'),
    path('reset/complete/', views.UserPassResetComplete.as_view(), name='reset_pass_complete'),
]



