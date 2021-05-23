from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy



class UserLogin(auth_views.LoginView):
    template_name='accounts/login.html'
    extra_context = {
        'name':'guest'
    }


class UserLogout(auth_views.LogoutView):
    next_page = 'library:list_books'



class UserPassReset(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:reset_pass_done')
    email_template_name = 'accounts/password_reset_email.html'



class UserPassResetDone(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'



class UserPassResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:reset_pass_complete')



class UserPassResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
