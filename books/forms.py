from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    title = forms.CharField()
    author = forms.CharField()
    description = forms.Textarea()

    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'description'
        ]
