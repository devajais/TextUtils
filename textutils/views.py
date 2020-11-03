# i created this file by my own-
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    #return HttpResponse('Home')
def removepunc(request):
    x = 0
    #Get the text
    djtext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    toupper = request.POST.get('toupper','off')

    if removepunc == 'on':
        analyzed=""
        punctutaions = '''!()-{}{};:,>./\?2@[]#$^&*'"_-`~'''
        for char in djtext:
            if char not in punctutaions:
                analyzed+=char
        params = {'purpose':'removed punctuation','analysed_text':analyzed}
    #analysed text
        x+=1
        djtext=analyzed
    if toupper=='on':
        analyzed = ""
        for char in djtext:
                analyzed += char.upper()
        params = {'purpose':'Upper case','analysed_text':analyzed}
        x+=1
    if x==0:
        return HttpResponse("Please check option")
    return render(request, 'analyse.html', params)
