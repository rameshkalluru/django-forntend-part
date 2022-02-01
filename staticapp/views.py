from django.shortcuts import render

# Create your views here.


def mark(request):
    return render(request,'mark.html')