from django.http import HttpResponse
import datetime


def hello(request):
    today = datetime.datetime.now()
    return HttpResponse(f"<h1>Hello Django </h1><h2>Today : {today} </h2>")
