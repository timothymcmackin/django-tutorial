from django.shortcuts import render
from django.http import HttpResponse

# return simple test string
def index(request):
    return HttpResponse("Test string!")
