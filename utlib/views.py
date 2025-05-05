from django.http import request, HttpResponse
import os
from django.conf import settings


def index(request):
    return HttpResponse("hello world")

def about(request):
    return HttpResponse("hi")

def test(request):
    return HttpResponse("test")

def home(request):
    return HttpResponse('finally done some part')

def hey(request):
    return HttpResponse("")