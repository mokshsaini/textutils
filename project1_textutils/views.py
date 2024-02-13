from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"index.html")
    

def analyse(request):

    remove_punc = request.POST.get("removepunc", "off") 
    remove_new_lines = request.POST.get("removenewlines" , "off")
    remove_extra_spaces = request.POST.get("removeextraspaces" , "off")
    num_of_characters  = request.POST.get("noofcharacters" , "off")
    uppercase = request.POST.get("uppercase" , "off")

    djtext = request.POST.get("text","default")

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyse = ""
    char_count = ""
    
    if (remove_punc == "on"):
        for char in djtext:
            if char not in punctuations:
                analyse = analyse + char
        djtext = analyse        

    if(remove_new_lines == "on"):
        analyse = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyse = analyse + char
        djtext = analyse

    if(remove_extra_spaces == "on"):
        analyse = ""
        for index , char in enumerate(djtext):
            if char == " " and djtext[index + 1] ==' ':
                pass
            else:
                analyse = analyse + char
        djtext = analyse    

    if(num_of_characters == "on"):
        analyse = ""
        i=0
        for char in djtext:
            if char != " " and char !='\n' and char != '\r':
                i+=1
        char_count = i

    if(uppercase == "on"):
        analyse = ""
        analyse = analyse + djtext.upper()
        djtext = analyse  

    if (remove_new_lines != "on" and remove_punc != "on" and remove_extra_spaces != "on" and num_of_characters != "on" and uppercase != "on" and djtext == ''):
        return HttpResponse("PLEASE ENTER THE TEXT AND CHOOSE ANY ONE OPTION:")

    if (remove_new_lines != "on" and remove_punc != "on" and remove_extra_spaces != "on" and num_of_characters != "on" and uppercase != "on"):
        return HttpResponse("PLEASE CHOOSE ANY ONE OPTION")

    if (djtext == ''):
        return HttpResponse("PLEASE ENTER THE TEXT:")

    
    return render(request,"analyse.html",{"dict":djtext , 'char_count':char_count , "num_of_characters":num_of_characters })

    