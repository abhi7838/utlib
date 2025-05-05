from django.http import request, HttpResponse
from django.shortcuts import render
import os
from django.conf import settings


def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    removespace = request.GET.get('removespace','off')
    upper = request.GET.get('upper','off')
    analyzed_main = ''
    if removepunc == 'on':
        analyzed = ''
        puntutions = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in puntutions:
                analyzed = analyzed+char
        params = {'purpse':'removed puntuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    # analyzed_main = analyze
    
    if removespace == 'on':
        analyzed = ''
        for char in djtext:
            if char != " ":
                analyzed +=char

        params = {'purpse':'removed puntuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    if upper =='on':
        analyzed = djtext.upper()
        params = {'purpse':'removed puntuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse('please select some task to complete on string')
def contact(request):
    return HttpResponse("hi this is contact page  hi ")

def index(request):
    return render(request,'index.html')
