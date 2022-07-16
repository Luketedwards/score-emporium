from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Genre
from .forms import ProductForm


# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    search_query = None

    if request.GET:
        if 'q' in request.GET:
            search_query = request.GET['q']
            if not search_query:
                messages.error(request, 'Please enter a search query.')
                return redirect(reverse('products'))

            queries = Q(name__icontains=search_query) | Q(description__icontains=search_query) | Q(vendor__icontains=search_query)  
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': search_query,
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


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.vendor = request.user.username
            obj.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)