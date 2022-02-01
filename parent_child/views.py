from django.shortcuts import render

# Create your views here.


def parentt(request):
    return render(request,'behara_parent.html')

def childd(request):
    return render(request,'behara_child.html')