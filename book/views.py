from django.http import HttpResponse
from django.shortcuts import render
from . import models


def helloview(request):
    return HttpResponse('Hello World')


def BooksView(request):
    books = models.Book.objects.all()
    context = {
        'book_objects': books
    }
    return render(request, 'books.html', context)