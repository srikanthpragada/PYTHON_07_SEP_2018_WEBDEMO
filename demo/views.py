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
                                          'trainer' :'Srikanth Pragada'})
