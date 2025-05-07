from django.http import request, HttpResponse
from django.shortcuts import render
import os
from django.conf import settings


# def analyze(request):
#     djtext = request.GET.get('text', 'default')
#     removepunc = request.GET.get('removepunc', 'off')
#     removespace = request.GET.get('removespace', 'off')
#     upper = request.GET.get('upper', 'off')

#     analyzed_main = djtext
#     purpose = ''

#     if removepunc == 'on':
#         punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
#         analyzed = ""
#         for char in analyzed_main:
#             if char not in punctuations:
#                 analyzed = analyzed + char
#         analyzed_main = analyzed
#         purpose += 'Removed Punctuations'
#         if removespace == 'on' or upper == 'on':
#             purpose += ' and '

#     if removespace == 'on':
#         analyzed = ""
#         for char in analyzed_main:
#             if char != " ":
#                 analyzed = analyzed + char
#         analyzed_main = analyzed
#         purpose += 'Removed Extra Spaces'
#         if upper == 'on':
#             purpose += ' and '

#     if upper == 'on':
#         analyzed_main = analyzed_main.upper()
#         purpose += 'Converted to Uppercase'

#     if removepunc == 'on' or removespace == 'on' or upper == 'on':
#         params = {'purpose': purpose, 'analyzed_text': analyzed_main}
#         return render(request, 'analyze.html', params)
#     else:
#         return HttpResponse('please select some task to complete on string')


def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    removespace = request.GET.get('removespace','off')
    upper = request.GET.get('upper','off')
    analyzed_main = djtext
    if removepunc == 'on' or removespace == 'on' or upper == 'on':
        if removepunc == 'on':
            analyzed = ''
            puntutions = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
            for char in djtext:
                if char not in puntutions:
                    analyzed = analyzed+char
            # params = {'purpse':'removed puntuations','analyzed_text':analyzed}
            # return render(request,'analyze.html',params)
            analyzed_main = analyzed

        if removespace == 'on':
            analyzed = ''
            for char in analyzed_main:
                if char != " ":
                    analyzed +=char

            # params = {'purpse':'removed puntuations','analyzed_text':analyzed}
            # return render(request,'analyze.html',params)
            analyzed_main = analyzed

        if upper =='on':
            analyzed = analyzed_main.upper()
            analyzed_main = analyzed


        params = {'purpse':'removed puntuations','analyzed_text':analyzed_main}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse('please select some task to complete on string')
    



def contact(request):
    return HttpResponse("hi this is contact page  hi ")

def index(request):
    return render(request,'index.html')
