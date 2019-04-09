from django.shortcuts import render
#from . import assignment 


def do(request):
    return render(request, 'myapp/do.html')

