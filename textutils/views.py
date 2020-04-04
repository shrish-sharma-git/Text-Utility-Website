# This file was created by me - Slim Shady
from django.http import HttpResponse
from django.shortcuts import  render

# HomePage
def index(request):
   return render(request, 'index.html')

# About Us
def aboutus(request):
    return render(request, 'About Us.html')

# features
def features(request):
    return render(request, 'features.html')

#AnNALyse Button Processes!!
def analyse(request):
    djtext= request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    remlwn = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    countchar = request.POST.get('countchar', 'off')

    # Removing Punctuations
    if removepunc == "on":
        punctuations ='''!(){}[];:'"/\,<>.?@#$%^&*_~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed += char
        params = {'purpose':'Removing Punctuations','analysed_text':analysed}
        djtext = analysed

    # Converting to Uppercase
    if fullcaps == "on":
        analysed = " "
        for char in djtext :
            analysed += char.upper()
        params = {'purpose': 'Changing to Uppercase', 'analysed_text': analysed}
        djtext = analysed
        #return render

    # Removing NewLine
    if remlwn == "on":
        analysed = " "
        for char in djtext:
            if char is not "\n" and char is not "\r":
                analysed += char
        params = {'purpose': 'Removing Newline', 'analysed_text': analysed}
        djtext = analysed

    # Removing Extra Spaces
    if spaceremover == "on":
        analysed = " "
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analysed += char
        params = {'purpose': 'Removing spaces', 'analysed_text': analysed}
        djtext = analysed
        #return render(request, 'analyse.html', params)

    # counting characters
    if countchar  == "on":
        analysed = " "
        count = 0
        for index, char in enumerate(djtext):
            count += 1
            analysed = count
        params = {'purpose': 'Counting characters', 'analysed_text': analysed}

    if removepunc != "on" and fullcaps != "on" and remlwn != "on" and spaceremover != "on" and countchar != "on":
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyse.html', params)

