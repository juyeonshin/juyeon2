from django.shortcuts import render

def main(request): 
     return render(request, 'main.html') 


 
def first(request): 
     return render(request, 'firstproject/first.html') 
 
 
def second(request): 
     return render(request, 'firstproject/second.html') 


def third(request): 
     return render(request, 'firstproject/third.html') 


