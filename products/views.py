from django.shortcuts import render

from products.models import Product, ProductStatus, ProductCategory, ProductTag


def products_list_view(request):
    context = {
        "products": Product.objects.filter(status=ProductStatus.AVAILABLE, is_active=True),
        "categories": ProductCategory.objects.filter(parent=None, is_active=True),
        "tags":ProductTag.objects.all(),
    }
    return render(request, 'products/products-list.html', context)


def products_detail_view(request, pk):
    try:
        product = Product.objects.get(id=pk, is_active=True)
    except Product.DoesNotExist:
        return render(request, 'shared/404.html')
    context = {
        "product": product,
    }
    return render(request, 'products/product-detail.html', context)




