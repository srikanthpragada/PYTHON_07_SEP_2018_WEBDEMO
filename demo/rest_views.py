from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'price', 'pubid')


@api_view(['GET', 'POST'])
def list_books(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    else:  # POST
        print("Adding new books", request.data)
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # insert row into table
            return Response(serializer.data, status = 201)

        return Response(serializer.errors, status=400)  # Bad request
