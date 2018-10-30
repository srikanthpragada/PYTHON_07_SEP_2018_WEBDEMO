from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Book
from django.db.models import Avg


def demo(request):
    return render(request, 'ajax_demo.html')


def now(request):
    return HttpResponse(str(datetime.now()))


def average_price(request):
    result = Book.objects.all().aggregate(average=Avg('price'))
    return HttpResponse( "%5.2d" % (result["average"]))
