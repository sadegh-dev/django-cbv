from .models import Comment
from django import forms


class LibraryCreateForm(forms.Form):
    title = forms.CharField(max_length=200)



class BookCommentsForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ('name','body')

