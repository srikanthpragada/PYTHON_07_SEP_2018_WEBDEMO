from django.shortcuts import render
from django.http import HttpResponse
from .models import Information


# Create your views here.

def index(request):
    # print(type(request))
    return HttpResponse("<h1>Demo Application</h1>")


def about(request):
    # render(request,template,context(dict))
    return render(request, 'about.html', {'info': Information(),
                                          'trainer': 'Srikanth Pragada'})


def interest(request):
    interest_amount = 0
    amount = 0
    period = 0
    if request.method == "POST":
        amount = int(request.POST["amount"])
        period = int(request.POST["period"])
        if period <= 12:
             rate = 6
        elif period <= 36:
             rate = 7
        else:
            rate = 8

        interest_amount = amount * rate / 100

    return render(request, 'interest.html',
                  {"amount": amount,
                   "period": period,
                   "interest" : interest_amount})
