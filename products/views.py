from django.shortcuts import render
from products.models import Product, ProductCategory, ProductTag, ProductColor, Manufacture


def products_list_view(request):
    products = Product.objects.filter(is_active=True)

    # Get filter values from URL
    category_id = request.GET.get('category')
    tag_id = request.GET.get('tag')
    color_id = request.GET.get('color')
    manufacture_id = request.GET.get('manufacture')

    # Apply filters if selected
    if category_id:
        products = products.filter(categories__id=category_id)

    if tag_id:
        products = products.filter(tags__id=tag_id)

    if color_id:
        products = products.filter(colors__id=color_id)

    if manufacture_id:
        products = products.filter(manufacture__id=manufacture_id)

    context = {
        "products": products,
        "categories": ProductCategory.objects.filter(is_active=True),
        "tags": ProductTag.objects.all(),
        "colors": ProductColor.objects.all(),
        "manufactures": Manufacture.objects.filter(is_active=True),
        "selected_category": category_id,
        "selected_tag": tag_id,
        "selected_color": color_id,
        "selected_manufacture": manufacture_id,
    }
    return render(request, 'products/products-list.html', context=context)


def products_detail_view(request, pk):
    try:
        product = Product.objects.get(pk=pk, is_active=True)
    except Product.DoesNotExist:
        return render(request, 'shared/404.html')

    context = {
        "product": product
    }
    return render(request, 'products/product-detail.html', context=context)