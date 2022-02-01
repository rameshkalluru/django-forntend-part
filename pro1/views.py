from django.shortcuts import render


def sample(request,input):
    return render(request,'sample.html')