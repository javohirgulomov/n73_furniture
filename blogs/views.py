from django.shortcuts import render
from blogs.models import Blog, BlogStatus, Category, Tag


def blogs_list_view(request):
    blogs = Blog.objects.filter(status=BlogStatus.PUBLISHED)

    # Get filter values from URL
    category_id = request.GET.get('category')
    tag_id = request.GET.get('tag')

    # Apply filters if selected
    if category_id:
        blogs = blogs.filter(categories__id=category_id)

    if tag_id:
        blogs = blogs.filter(tags__id=tag_id)

    context = {
        "blogs": blogs,
        "categories": Category.objects.filter(parent=None),
        "tags": Tag.objects.all(),
        "recent_posts": Blog.objects.filter(status=BlogStatus.PUBLISHED).order_by('-created_at')[:2],
        "selected_category": category_id,
        "selected_tag": tag_id,
    }
    return render(request, 'blogs/blogs-list.html', context)


def blog_detail_view(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        return render(request, 'shared/404.html')

    context = {
        "blog": blog
    }
    return render(request, 'blogs/blog-detail.html', context)