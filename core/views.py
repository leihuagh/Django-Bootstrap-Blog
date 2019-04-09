from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'base.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)
