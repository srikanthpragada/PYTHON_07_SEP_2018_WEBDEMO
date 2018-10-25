from django.shortcuts import render
from django.http import HttpResponse
from .models import Information
from . forms import PersonForm

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


def person_details(request):
    if request.method == "POST":
        f = PersonForm(request.POST)  # Bind request parameters to fields
        if f.is_valid():
            name = f.cleaned_data['fullname']
            email = f.cleaned_data['email']
            mobile = f.cleaned_data['mobile']
            age = f.cleaned_data['age']
            print(name,email,mobile,age)
        else:
            print("Invalid Data")
    else:
        f = PersonForm()   # Unbound form

    return render(request,'person_details.html',{'form' : f})