from django.shortcuts import render
from mainapp.models import ProductCategory, Product


def index(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    context = {
        'page_title': 'главная',
        'categories_menu': categories,
        'products': products,
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    context = {
        'page_title': 'каталог',
        'categories_menu': categories,
        'products': products,
    }
    return render(request, 'mainapp/catalog.html', context)


def contacts(request):
    contacts = [
        {
            'address': 'Кировская область, г. Киров, ул.Книжная, дом 77',
            'phone': '+7(777) 777-77-77',
            'email': 'kirovbooks@mail.ru',
        },
        {
            'address': 'Кировская область, г. Кирово-Чепецк, ул.Цветочная, дом 55',
            'phone': '+7(555) 555-55-55',
            'email': 'chepetskbooks@mail.ru',
        },
        {
            'address': 'Кировская область, г. Слободской, ул.Энтузиастов, дом 33',
            'phone': '+7(333) 333-33-33',
            'email': 'slobodabooks@mail.ru',
        },
    ]
    context = {
        'page_title': 'контакты',
        'contacts': contacts,
    }
    return render(request, 'mainapp/contacts.html', context)
