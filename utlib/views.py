from django.http import request, HttpResponse
import os
from django.conf import settings


def index(request):
    return HttpResponse("hi this is home page")

def about(request):
    return HttpResponse("hi this is about page")

def contact(request):
    return HttpResponse("hi this is contact page")

def home(request):
    return HttpResponse('finally done some part')

def hey(request):
    return HttpResponse("")