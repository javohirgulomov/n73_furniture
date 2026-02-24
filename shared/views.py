from django.shortcuts import render

from blogs.models import Author


def home_page_view(request):
    return render(request, 'shared/home.html')


def contact_page_view(request):
    return render(request, 'shared/contact.html')


def about_page_view(request):
    authors = Author.objects.filter(is_active=True).order_by('created_at')
    context = {'authors': authors}
    return render(request, 'shared/about-us.html', context)