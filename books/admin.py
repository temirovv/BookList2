from django.contrib import admin
from .models import Book
from .forms import BookForm


class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = [
        'title',
        'author',
        'description'
    ]
    list_filter = [
        "title",
        "author",
        'description'
    ]
    search_fields = [
        "title",
    ]

admin.site.register(Book, BookAdmin)
