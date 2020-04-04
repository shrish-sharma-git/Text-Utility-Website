# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render

# HomePage
def index(request):
    return render(request, 'index.html')

# About Us
def aboutus(request):
    return render(request, 'About Us.html')

# features
def features(request):
    return render(request, 'features.html')

def analyse(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numberremover = request.POST.get('numberremover', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char

        params = {'purpose': 'Removed Punctuations', 'analysed_text': analysed}
        djtext = analysed

    if (fullcaps == "on"):
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analysed_text': analysed}
        djtext = analysed

    if (extraspaceremover == "on"):
        analysed = ""
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                if not (djtext[index] == " "):
                    analysed = analysed + char

            elif not (djtext[index] == " " and djtext[index + 1] == " "):
                analysed = analysed + char

        params = {'purpose': 'Removed NewLines', 'analysed_text': analysed}
        djtext = analysed

    if (newlineremover == "on"):
        analysed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analysed = analysed + char

        params = {'purpose': 'Removed NewLines', 'analysed_text': analysed}

    if (numberremover == "on"):
        analysed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analysed = analysed + char

        params = {'purpose': 'Removed NewLines', 'analysed_text': analysed}
        djtext = analysed

    if (
            removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and numberremover != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyse.html', params)


