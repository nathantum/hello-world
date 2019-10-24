from django.shortcuts import render
from django.http import HttpResponse #new

# Create your views here.

# this function is new 
def homePageView(request):
    return HttpResponse("Hello, world!")
