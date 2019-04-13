from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect(settings.LOGIN_REDIRECT_URL + settings.LOGIN_URL)
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)
