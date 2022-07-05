from django.shortcuts import render
from products.models import Product

# Create your views here.

def user_profile(request):
    """ A view to return the index page """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'user_profile/profile.html', context)