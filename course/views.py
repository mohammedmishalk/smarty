from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def add_course(request):
    return HttpResponse("hallo")