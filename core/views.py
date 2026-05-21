from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')


def sobre(request):
    return render(request, 'core/sobre.html')


def contato(request):
    return render(request, 'core/contato.html')


def cod1(request):
    return render(request, 'core/codeum.html')

def cod2(request):
    return render(request, 'core/codedois.html')

def cod3(request):
    return render(request, 'core/codetres.html')