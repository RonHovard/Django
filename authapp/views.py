from django.shortcuts import render
from authapp.forms import ShopUserLoginForm


def user_login(request):
    form = ShopUserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'authapp/login.html', context)
