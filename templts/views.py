from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
        
def analyze(request):
    #get the text
    djtext = request.POST.get('text','def')  #CSRF -> Cross Site Request Forgery - CSRF is by default used by django ,for the security purpose , it makes sure that all the commands are sent by your website only and not other's.
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')    
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    print(removepunc)
    print(djtext)
    # analyzed = djtext
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
    analyzed = "" 
    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Change to Uppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char!= '\r':      #even if this line is not written still the newlineremover will work LOL
                analyzed = analyzed + char 
        params = {'purpose':'Remove NewLine','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif extraspaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
             
        params = {'purpose':'Extra Space Remover','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif charcount == 'on':
        analyzed = print(len(text))   
        params = {'purpose':'Character Count','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse("Error")
    #Analyse the text
    #return HttpResponse("removepunc")
   

# def capitalizefirst(request):
#     return HttpResponse("capitalize first")

