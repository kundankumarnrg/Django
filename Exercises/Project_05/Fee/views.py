from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fee_details(request):
    return HttpResponse("<h1>Fee Details...!<h1>")