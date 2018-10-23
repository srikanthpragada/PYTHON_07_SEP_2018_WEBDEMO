from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import datetime


def list_movies(request):
    # Look for a cookie with name city
    print(request.COOKIES)
    if 'city' in request.COOKIES:
        cityname = request.COOKIES['city']
        return HttpResponse(f"<h1>List Of Movies in {cityname}</h1>")
    else:
        return redirect("/demo/selectcity")


def select_city(request):
    if request.method== "POST":
        city = request.POST["city"]
        # Create a cookie and send it to client
        response = HttpResponseRedirect("/demo/movies/")
        response.set_cookie("city", city,
                  expires = datetime.datetime.now() + datetime.timedelta(days=10))
        return response
    else:
        return render(request,'selectcity.html')
