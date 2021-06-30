from django.shortcuts import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse('Hello Universe, This is our first alien meeting. behave yourself or get expelled')

