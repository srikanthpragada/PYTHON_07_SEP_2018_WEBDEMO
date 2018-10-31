from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Book
from .forms import AddBookForm


def list_books(request):
    books = Book.objects.all()
    return render(request, 'books/list.html', {'books': books})


def add_book(request):
    message = ''
    if request.method == "POST":
        f = AddBookForm(request.POST)
        if f.is_valid():
            f.save()
            message = "Book has been added successfully!"
    else:
        f = AddBookForm()

    return render(request, 'books/add.html', {'form': f, 'message': message})


def delete_book(request, bookid):
    message = ''
    try:
        book = Book.objects.get(id=bookid)
        book.delete()
        message = f"Book [{bookid}] has been deleted!"
    except:
        message = f"Book [{bookid}] was not found!"

    return render(request, 'books/delete.html', {'message': message})


def edit_book(request, bookid):
    message = ''
    if request.method == "POST":
        try:
            book = Book.objects.get(id=bookid)
            f = AddBookForm(request.POST, instance=book)
            if f.is_valid():
                # book.title = f.cleaned_data["title"]
                # book.price = f.cleaned_data["price"]
                # book.pubid = f.cleaned_data["pubid"]
                book.save()  # Update table
                message = "Updated book successfully!"
        except:
            message = f"Error during updation of book - {bookid}"
    else:
        try:
            book = Book.objects.get(id=bookid)
            # f = AddBookForm({'title': book.title, 'price': book.price, 'pubid': book.pubid})
            f = AddBookForm(instance=book)
        except:
            message = f"Book [{bookid}] was not found!"

    return render(request, 'books/edit.html', {'form': f, 'message': message})


def search_form(request):
    return render(request, 'books/search.html')


def search_books(request):
    title = request.GET["title"]
    # Get QuerySet of  dict with two keys - title and price
    books = Book.objects.filter(title__contains=title).values("title","price")
    # Convert QuerySet to list
    books_list = list(books);
    return JsonResponse(books_list, safe=False)
