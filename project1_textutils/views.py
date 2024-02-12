from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    dict = {"name":"moksh", "mission":"mars"}
    return render(request,"index.html",dict)
    

def removepunc(request):
    return HttpResponse("removepunc <br> <a href=\"http://127.0.0.1:8000\"> Back </a>")

def capitalizefirst(request):
    return HttpResponse("capitalizefirst <br> <a href=\"http://127.0.0.1:8000\"> Back </a>")

def newlineremove(request):
    return HttpResponse("newlineremove <br> <a href=\"http://127.0.0.1:8000\"> Back </a>")

def spaceremove(request):
    return HttpResponse("spaceremove <br> <a href=\"http://127.0.0.1:8000\"> Back </a>")

def charcount(request):
    return HttpResponse("charcount <br> <a href=\"http://127.0.0.1:8000\"> Back </a>")

def analyse(request):
    remove_punc = request.GET.get("removepunc", "off") 
    remove_new_lines = request.GET.get("removenewlines" , "off")
    remove_extra_spaces = request.GET.get("removeextraspaces" , "off")
    num_of_characters  = request.GET.get("noofcharacters" , "off")
    uppercase = request.GET.get("uppercase" , "off")
    djtext = request.GET.get("text","default")
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyse = ""
    if remove_punc == "on":
        for char in djtext:
            if char not in punctuations:
                analyse = analyse + char
    
        return render(request,"analyse.html",{"dict":analyse})

    if(remove_new_lines == "on"):
        for char in djtext:
            if char != "\n" and char != "\r":
                analyse = analyse + char
        return render(request,"analyse.html",{"dict":analyse})

    if(remove_extra_spaces == "on"):
        for char in djtext:
            if char != "  " and char !='\n':
                analyse = analyse + char
        return render(request,"analyse.html",{"dict":analyse})
    
    if(num_of_characters == "on"):
        i=0
        for char in djtext:
            if char != " " and char !='\n':
                i+=1
        return HttpResponse(f"<h1>no. of characters are :{i}</h1>")

    if(uppercase == "on"):
            analyse = analyse + djtext.upper()
            return render(request,"analyse.html",{"dict":analyse})
    
    else:
        return HttpResponse("error")
    