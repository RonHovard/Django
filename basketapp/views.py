from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import BasketSlot
from mainapp.models import Product


def basket(request):
    content = {}
    return render(request, 'basketapp/basket.html', content)


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket_slot = BasketSlot.objects.filter(user=request.user, product=product).first()

    if not basket_slot:
        basket_slot = BasketSlot(user=request.user, product=product)

    basket_slot.quantity += 1
    basket_slot.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request):
    pass
