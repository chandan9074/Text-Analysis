from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index (request):
    
    return render(request, 'index.html')
    
    #return HttpResponse("<h3>Hello chandan</h3>"'''<a href = "http://127.0.0.1:8000/chandan/">Go to Chandan</a>''')


def chandan (request):

    
    
    djtext = request.POST.get('text', 'off')
    mithun = request.POST.get('mithun', 'off')
    djupper = request.POST.get('capital', 'off')
    djnew = request.POST.get('newline', 'off')
    djex = request.POST.get('exspace', 'off')
    djchar = request.POST.get('char', 'off')
    if mithun == "on":
        punc = '''[]{}-!"#$%&'()*+,./:;<=>?@\^_`|\''''

        analyzed = ""
   
        for char in djtext:
              if char  not in punc:
               analyzed = analyzed + char  

        dic1 = {'heading': 'Finally we got our expected output', 'analyzed_text' : analyzed}
        djtext = analyzed
        #return render(request,'analyzed.html', dic)
    if (djupper == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        dic1 = { 'heading':'Now you can see everything in uppercase!!!','analyzed_text': analyzed}
        djtext = analyzed
        #return render(request,'analyzed.html', dic1)    
    
    if (djnew == "on"):
        analyzed = ""
        for char in djtext:
            if char !=('\n') and char !=("\r"):
                analyzed = analyzed + char
        dic1 = { 'heading':'Now you can see everything in one line!!!','analyzed_text': analyzed}
        djtext = analyzed
        #return render(request,'analyzed.html', dic1)
    
    if (djex == "on"):
        analyzed = ""
        n = 0
        for char in djtext:
            if char == " " and n<2:
                analyzed = analyzed + char
                n = 2
                continue
            if char != " ":
                analyzed = analyzed + char
                n = 1
        dic1 = { 'heading':'Now you can see everything in perfect formet!!!','analyzed_text': analyzed}
        djtext = analyzed 
        #return render(request,'analyzed.html', dic1)
    
    if (djchar == "on"):
        analyzed = ""
        analyzed = djtext
        djtext = djtext.upper()
        n = 0
        for char in djtext:
            if char>='A' and char<="Z":
                n = n+1
        
        dic1 = { 'heading':'Now you can see how many charecter in this text!!!','analyzed1_text': n, 'result': 'Ruselt = ', 'analyzed_text':analyzed}
        
        # return render(request,'analyzed.html', dic1)

    #else:
    #return render(request, 'analyzed.html', dic1)
     #   return HttpResponse('Error')    
    if (mithun != "on" and djupper != "on" and djnew != "on" and djex != "on" and djchar != "on"):
        dic2 = {'error': 'Please, Atfirst select any option....'}
        return render(request, 'analyzed.html', dic2)
    
    else:
        return render(request, 'analyzed.html', dic1)

def aboutus (request) :
    
     return render(request, 'aboutus.html')
 
def contactus (request):
    return render(request, 'contact.html')
 
    #return HttpResponse("<h3>Yes!! I am Chandan</h3>"'''<a href = "http://127.0.0.1:8000/mithun/">Go to Mithun</a>''')

#def mithun (request):
 #   return HttpResponse("<h3>Yes!! I am Mithun</h3>" '''<a href = "http://127.0.0.1:8000/">Back to Home</a>''')