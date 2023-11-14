from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sudheer(request):
    return HttpResponse('<marquee><h1>hii raju how r u</h1></marquee>')
