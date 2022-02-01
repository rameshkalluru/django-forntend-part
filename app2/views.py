from django.shortcuts import render

# Create your views here.
def ramya(request,input):
    return render(request,'ramya.html',{"data":input})