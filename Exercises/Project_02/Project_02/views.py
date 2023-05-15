from django.shortcuts import render
from django.http import HttpResponse


def show_message(request):
    return HttpResponse("<h1>Success full run...!</h1>")
