from django.shortcuts import render



def home(request):
    return render(request, 'home.html')

def home2(request):
    return render(request, 'home2.html')

def home3(request):
    return render(request, 'home3.html')

def home4(request):
    return render(request, 'home4.html')

def home5(request):
    return render(request, 'home5.html')

def blogs_list(request):
    return render(request, 'blogs-list.html')

def blog_list_sidebar_left2(request):
    return render(request, 'blog-list-sidebar-left2.html')

def blog_list_sidebar_right(request):
    return render(request, 'blog-list-sidebar-right.html')

def blog_list_no_sidebar(request):
    return render(request, 'blog-list-no-sidebar.html')

def blog_grid_no_sidebar(request):
    return render(request, 'blog-grid-no-sidebar.html')

def blog_detail(request):
    return render(request, 'blog-detail.html')

def products_list(request):
    return render(request, 'products-list.html')

def product_grid_sidebar_right(request):
    return render(request, 'product-grid-sidebar-right.html')

def product_list_sidebar_left(request):
    return render(request, 'product-list-sidebar-left.html')

def product_detail(request):
    return render(request, 'product-detail.html')

def account(request):
    return render(request, 'account.html')

def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

# Other pages
def contact(request):
    return render(request, 'contact.html')

def about_us(request):
    return render(request, 'about-us.html')

def page_404(request):
    return render(request, '404.html')

def handler404(request, exception):
    return render(request, '404.html', status=404)

