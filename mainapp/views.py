from django.shortcuts import render, get_object_or_404
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


def catalog(request, pk=None):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    if pk:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = products.filter(category=category)
        context = {
            'page_title': category.name,
            'categories_menu': categories,
            'products': products,
        }
        url_name = 'mainapp/category.html'
    else:
        context = {
            'page_title': 'каталог',
            'categories_menu': categories,
            'products': products,
        }
        url_name = 'mainapp/catalog.html'
    return render(request, url_name, context)


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


def product(request, pk):
    categories = ProductCategory.objects.all()
    _product = get_object_or_404(Product, pk=pk)
    context = {
        'page_title': 'Книга',
        'categories_menu': categories,
        'product': _product,
    }
    return render(request, 'mainapp/product.html', context)
