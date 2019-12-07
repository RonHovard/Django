from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('catalog/', mainapp.catalog, name='catalog'),
    path('contacts/', mainapp.contacts, name='contacts'),
    path('catalog/category/<int:pk>/', mainapp.catalog, name='category'),
    path('catalog/product/<int:pk>/', mainapp.product, name='product'),
]
