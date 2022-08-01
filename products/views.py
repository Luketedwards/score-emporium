from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Genre
from .forms import ProductForm
from user_profile.models import UserProfile
import pypdfium2 as pdfium
from PIL import Image, ImageFilter, ImageFont, ImageDraw


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
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    

    product = get_object_or_404(Product, pk=product_id)
    username= product.vendor
    queries = Q(vendor__iexact=username)  
    products = Product.objects.all()
    relevant_products = products.filter(queries)
    product_number = relevant_products.count()
    purchased_scores = UserProfile.purchased_scores
    
    context = {
        'product': product,
        'products': products,
        'product_number': product_number,
        'relevant_products': relevant_products,
        'purchased_scores': purchased_scores,
        'orders': orders,
    }

    return render(request, 'products/product_details.html', context)


def guitar_pro(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    username= product.vendor
    queries = Q(vendor__iexact=username)  
    products = Product.objects.all()
    relevant_products = products.filter(queries)
    product_number = relevant_products.count()
    
    context = {
        'product': product,
        'products': products,
        'product_number': product_number,
        'relevant_products': relevant_products
    }

    return render(request, 'products/my_scores.html', context)    

@login_required
def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.vendor = request.user.username
                
            obj.save()
            if not obj.image:
                obj = form.save(commit=False)
                
                font = ImageFont.truetype('fonts/PlayfairDisplay-Bold.ttf', 400)
                text = 'Sample'

                filepath = obj.PDF.path
                pdf = pdfium.PdfDocument(filepath)
                page = pdf.get_page(0)
                pil_image = page.render_topil()
                pil_image.save(f"{obj.name}-{obj.vendor}.jpg")
                page.close()

                image = Image.open(f'{obj.name}-{obj.vendor}.jpg')
                cropped_image = image.crop((5,1673,2459,3013))
                blurred_image = cropped_image.filter(ImageFilter.GaussianBlur(radius=10))
                image.paste(blurred_image,(5,1673,2459,3013))
                editImage = ImageDraw.Draw(image)
                editImage.text((550,1400), text,(84, 83, 82), font=font)
                final_image= image.save(f'media/{obj.name}-image.jpg')
                obj.image = final_image
                obj.save()

            
            
                

              
            product = obj.save()
            
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    products = Product.objects.all()
    username= request.user.username
    queries = Q(vendor__iexact=username)  
    products = products.filter(queries)
    product_number = products.count()

    context = {
        'form': form,
        'product_number':product_number
    }

    return render(request, template, context)
    

@login_required    
def add_product_store(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.vendor = request.user.username
            if not obj.image:
                pages = convert_from_path(obj.PDF)
                for page[0] in pages:
                    page.save('pdfimage.jpg', 'JPEG')


            obj.save()
            product = obj.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('storefront'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    products = Product.objects.all()
    username= request.user.username
    queries = Q(vendor__iexact=username)  
    products = products.filter(queries)
    product_number = products.count()
    
    context = {
        'form': form,
        'product_number':product_number
    }

    return render(request, template, context)    

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    username = request.user.username

    product = get_object_or_404(Product, pk=product_id)
    if username == product.vendor:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully updated product!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to update product. Please ensure the form is valid.')
        else:
            form = ProductForm(instance=product)
            messages.info(request, f'You are editing {product.name}')
    else:
        messages.error(request, 'You are not authorised to edit this product')
        return redirect(reverse('product_detail', args=[product.id]))
          

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_product_store(request, product_id):
    """ Edit a product in the store """
    username = request.user.username

    product = get_object_or_404(Product, pk=product_id)
    if username == product.vendor:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully updated product!')
                return redirect(reverse('storefront'))
            else:
                messages.error(request, 'Failed to update product. Please ensure the form is valid.')
        else:
            form = ProductForm(instance=product)
            messages.info(request, f'You are editing {product.name}')
    else:
        messages.error(request, 'You are not authorised to edit this product')
        return redirect(reverse('product_detail', args=[product.id]))
          

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)    


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    username = request.user.username

    product = get_object_or_404(Product, pk=product_id)
    if username == product.vendor:
        product.delete()
        messages.success(request, f'{product.name} was deleted.')
        return redirect(reverse('products'))   
    else:
        messages.error(request, 'You are not authorised to delete this product')
        return redirect(reverse('product_detail', args=[product.id]))


@login_required
def delete_product_store(request, product_id):
    """ Delete a product from the store """
    username = request.user.username

    product = get_object_or_404(Product, pk=product_id)
    if username == product.vendor:
        product.delete()
        messages.success(request, f'{product.name} was deleted.')
        return redirect(reverse('storefront'))   
    else:
        messages.error(request, 'You are not authorised to delete this product')
        return redirect(reverse('product_detail', args=[product.id]))        
