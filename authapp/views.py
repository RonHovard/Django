from django.contrib import auth
from django.urls import reverse
from authapp.forms import ShopUserLoginForm
from django.shortcuts import render
from django.http import HttpResponseRedirect


def user_login(request):
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = ShopUserLoginForm()

    context = {
        'page_title': 'вход в систему',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)