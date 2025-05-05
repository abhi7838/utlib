from django.http import request, HttpResponse
from django.shortcuts import render
import os
from django.conf import settings


def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    # return render(request,'index.html')
    if removepunc == 'on':
        puntutions = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in puntutions:
                analyzed = analyzed+char
        params = {'purpse':'removed puntuations','analyzed_text':analyzed}

        return render(request,'analyze.html',params)

    else:
        return HttpResponse('please select some task to complete on string')

def contact(request):
    return HttpResponse("hi this is contact page  hi ")

# def punc(request):
#     return render(request,'index.html')
    # return HttpResponse('hey this is home page')
def index(request):
    return render(request,'index.html')
    # return HttpResponse('hey this is home page')