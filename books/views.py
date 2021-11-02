from django.shortcuts import render
from django.core.paginator import (Paginator,
                                   EmptyPage,
                                   PageNotAnInteger)
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Book
from .admin import BookForm


def index(request):

    books = Book.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(books, 3)

    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'pages': pages})


def create(request):
    form_of_book = BookForm(request.POST or None)

    if form_of_book.is_valid():
        form_of_book.save()
        return HttpResponseRedirect(reverse('books.home'))

    return render(request, 'create.html', {'form': form_of_book})


def delete(request, pk):

    book = Book.objects.all().get(id=pk)
    book.delete()
    return HttpResponseRedirect(reverse('books.home'))


def update(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return HttpResponseRedirect(reverse('books.home'))
    form_of_book = BookForm(request.POST or None, instance=book)

    if form_of_book.is_valid():
        form_of_book.save()
        return HttpResponseRedirect(reverse("books.home"))

    return render(request, 'update.html', {'form': form_of_book})
