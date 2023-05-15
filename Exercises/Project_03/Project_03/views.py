from django.shortcuts import render
from django.http import HttpResponse


def java_book_price(requet):
    return HttpResponse("Java :200")

def python_book_price(request):
    return HttpResponse("<h1>Python :500</h1>")

def mysql_book_prince(request):
    price="mysql : 300"
    return HttpResponse(price)

def total_price(request):
    total=200+500+300
    return HttpResponse("Total Book priece {}, {}, and {} are :{}".format("Java","Python","Mysql",total))