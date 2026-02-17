from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def products_list_view(request):
    return render(request, 'products/products-list.html')