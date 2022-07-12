from django.shortcuts import render
from django.db.models import Q
from products.models import Product

# Create your views here.

def user_profile(request):
    """ A view to return the index page """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'user_profile/profile.html', context)

def user_store(request):
    """ A view to return the index page """
    products = Product.objects.all()
    username= request.GET['username']
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
        