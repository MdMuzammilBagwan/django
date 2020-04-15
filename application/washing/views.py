from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context={
        'variable':'sent'
    }
    return render(request,'index.html',context)
def about(request):
    return(HttpResponse("hello"))

# Create your views here.
    