from django.shortcuts import render, redirect

from . models import  Book


def list(request):
    books = Book.objects.all()
    return render(request, 'books/list.html', {'books' : books})


def add(request):
    return render(request, 'books/add.html')



