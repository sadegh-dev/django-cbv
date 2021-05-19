from django import forms


class LibraryCreateForm(forms.Form):
    title = forms.CharField(max_length=200)





