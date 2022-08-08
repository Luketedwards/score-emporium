from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from products.models import Product
from .models import UserProfile

# Create your views here.

def user_profile(request):
    """ A view to return the index page """
    profile = get_object_or_404(UserProfile, user=request.user)
    products = Product.objects.all()
    orders = profile.orders.all()

    context = {
        'products': products,
        'profile': profile,
        'orders': orders
    }

    return render(request, 'user_profile/profile.html', context)

def user_store(request):
    """ A view to return the users store """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    products = Product.objects.all()
    all_products = products
    username= request.user.username
    queries = Q(vendor__iexact=username)  
    products = products.filter(queries)
    product_number = products.count()
    purchased_scores = UserProfile.purchased_scores

    context = {
        'products': products,
        'username': username,
        'product_number': product_number,
        'purchased_scores': purchased_scores,
        'all_products': all_products,
        'profile': profile,
        'orders': orders
    }

    if username == request.user.username:
        return render(request, 'user_profile/my_storefront.html', context) 
    else:
        return render(request, 'user_profile/other_storefront.html', context) 
        

def other_store(request, username):
    """ A view to return the users store """
    products = Product.objects.all()
    username= username
    queries = Q(vendor__iexact=username)  
    products = products.filter(queries)
    product_number = products.count()

    context = {
        'products': products,
        'username': username,
        'product_number': product_number
    }

    if username == request.user.username:
        return render(request, 'user_profile/my_storefront.html', context) 
    else:
        return render(request, 'user_profile/other_storefront.html', context)         

        