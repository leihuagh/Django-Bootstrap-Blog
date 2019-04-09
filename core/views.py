from django.shortcuts import render


def index(request):
    context = {
        'title': 'Welcome',
        'page_title': 'Home Index',
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'title': 'About Us',
        'page_title': 'About Us Page',
    }
    return render(request, 'index.html', context)


def contact(request):
    context = {
        'title': 'Contact Us',
        'page_title': 'Contact Us Page',
    }
    return render(request, 'index.html', context)
