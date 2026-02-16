"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path

from shared import views

urlpatterns = [
    # Home pages
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('home2/', views.home2, name='home2'),
    path('home3/', views.home3, name='home3'),
    path('home4/', views.home4, name='home4'),
    path('home5/', views.home5, name='home5'),

    # Blog pages
    path('blogs-list/', views.blogs_list, name='blogs-list'),
    path('blog-list-sidebar-left2/', views.blog_list_sidebar_left2, name='blog-list-sidebar-left2'),
    path('blog-list-sidebar-right/', views.blog_list_sidebar_right, name='blog-list-sidebar-right'),
    path('blog-list-no-sidebar/', views.blog_list_no_sidebar, name='blog-list-no-sidebar'),
    path('blog-grid-no-sidebar/', views.blog_grid_no_sidebar, name='blog-grid-no-sidebar'),
    path('blog-detail/', views.blog_detail, name='blog-detail'),

    # Product pages
    path('products-list/', views.products_list, name='products-list'),
    path('product-grid-sidebar-right/', views.product_grid_sidebar_right, name='product-grid-sidebar-right'),
    path('product-list-sidebar-left/', views.product_list_sidebar_left, name='product-list-sidebar-left'),
    path('product-detail/', views.product_detail, name='product-detail'),

    # User account pages
    path('account/', views.account, name='account'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('wishlist/', views.wishlist, name='wishlist'),

    # Shopping pages
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    # Other pages
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about_us, name='about-us'),
    path('404/', views.page_404, name='404'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

