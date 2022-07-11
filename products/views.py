from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    products = Product.objects.all()
    product_number = Product.objects.filter(vendor=product.vendor).count()
    context = {
        'product': product,
        'products': products,
        'product_number': product_number,
    }

    return render(request, 'products/product_details.html', context)    