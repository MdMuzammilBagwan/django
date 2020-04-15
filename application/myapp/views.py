from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'index.html',{'name':'Navin'})
def about(request):
    val1= int(request.GET['num1'])
    val2= int(request.GET['num2'])
    res =val1 + val2
    return render(request,'index.html',{'result':res})
def  remove(request):                    
    return render(request,'results.html')

