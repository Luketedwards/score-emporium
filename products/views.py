from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum

from score_emporium.settings import MEDIA_URL, UPLOAD_ROOT, AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID, AWS_STORAGE_BUCKET_NAME  
from .models import Product, Genre, Review
from .forms import ProductForm
from user_profile.models import UserProfile
import pypdfium2 as pdfium
from PIL import Image, ImageFilter, ImageFont, ImageDraw

from django.core.files.storage import FileSystemStorage
import os


# Create your views here.


# creating global instance of amazon S3 bucket for file uploads
def _get_s3_resource():
    if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
        return boto3.resource(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
    else:
        return boto3.resource('s3')


# the projects Amazon S3 bucket
def get_bucket():
    s3_resource = _get_s3_resource()
    return s3_resource.Bucket(AWS_STORAGE_BUCKET_NAME)

def upload_file_s3(image,newPath):
    # uploads file to S3 bucket
    my_bucket = get_bucket()
    my_bucket.Object(newPath).put(Body=image)   
    return 'file uploaded' 



def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    search_query = None

    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        orders = profile.orders.all()

    else:
        orders=None    
    
    if request.user.is_authenticated:
        ordersList = []

        for order in orders:
            for item in order.lineitems.all():
                ordersList.append(item.product.id)
    else:
        ordersList=[]            

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
        'orderslist': ordersList
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        orders = profile.orders.all()

    else:
        orders=None    
    
    ordersList = []

    for order in orders:
        for item in order.lineitems.all():
            ordersList.append(item.product.id)


    product = get_object_or_404(Product, pk=product_id)
    username= product.vendor
    queries = Q(vendor__iexact=username)  
    products = Product.objects.all()
    relevant_products = products.filter(queries)
    product_number = relevant_products.count()
    purchased_scores = UserProfile.purchased_scores
    all_reviews = Review.objects.filter(product=product)
    total_score = all_reviews.aggregate(total_score=Sum('ratings'))['total_score']
    
    review_count = all_reviews.count()
    review_count_5 = all_reviews.filter(ratings=5).count()
    review_count_4 = all_reviews.filter(ratings=4).count()
    review_count_3 = all_reviews.filter(ratings=3).count()
    review_count_2 = all_reviews.filter(ratings=2).count()
    review_count_1 = all_reviews.filter(ratings=1).count()

    if review_count_5 > 0:
        percent_5 = review_count_5 / review_count 
        percent_5 = percent_5 * 100
    else:
        percent_5 = 0    
    if review_count_4 > 0:
        percent_4 = review_count_4 / review_count
        percent_4 = percent_4 * 100
    else:
        percent_4 = 0 
    if review_count_3 > 0:
        percent_3 = review_count_3 / review_count 
        percent_3 = percent_3 * 100
    else:
        percent_3 = 0 
    if review_count_2 > 0:
        percent_2 = review_count_2 / review_count
        percent_2 = percent_2 * 100
    else:
        percent_2 = 0 
    if review_count_1 > 0:
        percent_1 = review_count_1 / review_count
        percent_1 = percent_1 * 100
    else:
        percent_1 = 0 

    average_rating = 0

    if review_count > 0:
        average_rating = total_score / review_count  
        product.rating = average_rating
        product.save()
    
    context = {
        'product': product,
        'products': products,
        'product_number': product_number,
        'relevant_products': relevant_products,
        'purchased_scores': purchased_scores,
        'orders': orders,
        'all_reviews': all_reviews,
        'review_count': review_count,
        'average_rating': average_rating,
        'total_score': total_score,
        'percent_5': percent_5,
        'percent_4': percent_4,
        'percent_3': percent_3,
        'percent_2': percent_2,
        'percent_1': percent_1,
        'review_count_5': review_count_5,
        'review_count_4': review_count_4,
        'review_count_3': review_count_3,
        'review_count_2': review_count_2,
        'review_count_1': review_count_1,
        'ordersList': ordersList,
    }

    if request.method == 'POST':
        ratings = request.POST.get('ratings')
        ratings = int(ratings)
        subject = request.POST.get('subject')
        content = request.POST.get('content')


        if content:
            reviews = Review.objects.filter(created_by=request.user, product=product)
            if reviews.count() > 0:
                review=reviews.first()
                review.delete()
                review = Review.objects.create(
                    product=product,
                    ratings=int(ratings),
                    subject=subject,
                    content=content,
                    created_by=request.user,
                )
                

            else:
                
                review = Review.objects.create(
                    product=product,
                    ratings=int(ratings),
                    subject=subject,
                    content=content,
                    created_by=request.user,
                )

            

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
            name = f"{obj.name}"
            name2 = obj.PDF.name
            new_name = name.replace(" ","-")
            new_name2 = name2.replace(" ","-")
            if not obj.image:
                font = ImageFont.truetype('fonts/PlayfairDisplay-Bold.ttf', 400)
                font2 = ImageFont.truetype('fonts/PlayfairDisplay-Bold.ttf', 100)
                text = 'Sample'
                text2 = f'© {obj.vendor}'

                fs = FileSystemStorage(location=UPLOAD_ROOT, base_url='/uploads')
                pdfFile = fs.save(f"{new_name}-{obj.vendor}.pdf", obj.PDF)
                pdfPath = fs.path(pdfFile)



                pdf = pdfium.PdfDocument(pdfPath)
                page = pdf.get_page(0)
                pil_image = page.render_topil()
                pil_image.save(f"pil-{obj.name}-{obj.vendor}.jpg")
                page.close()

                image = Image.open(f'pil-{obj.name}-{obj.vendor}.jpg')
                cropped_image = image.crop((5,1673,2459,3313))
                blurred_image = cropped_image.filter(ImageFilter.GaussianBlur(radius=10))
                image.paste(blurred_image,(5,1673,2459,3313))
                editImage = ImageDraw.Draw(image)
                editImage.text((550,2100), text,(84, 83, 82), font=font)
                editImage2 = ImageDraw.Draw(image)
                editImage2.text((850,2600), text2,(84, 83, 82), font=font2)
                
                newPath = f'blur-{new_name}-{obj.vendor}-image.jpg'
                upload_file_s3(image, newPath)
                
                
                
                os.remove(f"pil-{obj.name}-{obj.vendor}.jpg")
                obj.image.name = f'{MEDIA_URL}blur-{new_name}-{obj.vendor}-image.jpg'
                

            # rename the pdf file
            obj.Guitar_Pro_Unlocked.name = f'guitar-pro-{new_name}-{obj.vendor}.gp'
            obj.PDF = request.FILES['PDF']
            obj.PDF.name = f'{new_name}-{obj.vendor}.pdf'
              
            obj.save()
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
        context ={
            'storevendor': username
        }
        return redirect(reverse('storefront', storevendor=request.user.username))   
    else:
        messages.error(request, 'You are not authorised to delete this product')
        return redirect(reverse('product_detail', args=[product.id]))        
