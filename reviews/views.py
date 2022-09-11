from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from .models import Review




# Create your views here.


def productReview(request, product_id):
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


    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        rating = request.POST.get('rating', 0)
        content = request.POST.get('content','')


        if content:
            reviews = Review.objects.filter(created_by=request.user, product=product)
            if reviews.count() > 0:
                review=reviews.first()
                review.rating = rating,
                review.content = content,
                review.save()

            else:
                
                review = Review.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    created_by=request.user,
                )

            
            return render(request, 'products/product_details.html', context)

