from django.shortcuts import render
from blogs.models import Author


def home(request):
    return render(request, 'index.html')


def about(request):

    authors = Author.objects.filter(is_active=True).order_by('created_at')

    context = {
        'authors': authors,
    }

    return render(request, 'shared/about-us.html', context)