from email import message

from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from products.models import Product
from .models import UserProfile
from .forms import vendorForm, UserProfileForm
from django.contrib import messages


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

def user_store(request, storevendor):
    """ A view to return the users store """
    if request.user.username == storevendor:
        
        profile = get_object_or_404(UserProfile, user=request.user)
    else: 
        user2 = get_object_or_404(User , username=storevendor)

        profile = get_object_or_404(UserProfile, user=user2)    
    orders = profile.orders.all()
    
    vendor_profile = profile
    # get all products 
    vendor_products = Product.objects.all()
    vendor_average_rating= 0
    reviewed_products = 0
    for products in vendor_products:
        if products.vendor == storevendor and products.rating:
            vendor_average_rating = vendor_average_rating + products.rating
            reviewed_products = reviewed_products + 1 
    final_average = vendor_average_rating / reviewed_products
    vendor_profile.average_rating = final_average  
    vendor_profile.save()

    # round vendor average rating to 1 decimal place and the nearest .5
    vendor_average_rating = vendor_profile.average_rating
    vendor_average_rating = round(vendor_average_rating * 2) / 2
    vendor_average_rating = round(vendor_average_rating, 1)

    if request.user.is_authenticated:
        
        orders2 = profile.orders.all()

    else:
        orders2=None    
    
    ordersList = []

    for order in orders2:
        for item in order.lineitems.all():
            ordersList.append(item.product.id)

    products = Product.objects.all()
    all_products = products
    username= request.user.username
    queries = Q(vendor__iexact=storevendor)  
    products = products.filter(queries)
    product_number = products.count()
    purchased_scores = UserProfile.purchased_scores
    sales_number = profile.sales_number
    sales_income = profile.sales_income
    money_due = profile.money_due

    context = {
        'products': products,
        'username': username,
        'product_number': product_number,
        'purchased_scores': purchased_scores,
        'all_products': all_products,
        'profile': profile,
        'orders': orders,
        'sales_number':sales_number,
        'sales_income':sales_income,
        'money_due':money_due,
        'storevendor':storevendor,
        'ordersList':ordersList,
        'vendor_average_rating':vendor_average_rating,

    }

    if username == storevendor:
        if profile.vendor == True:
            return render(request, 'user_profile/my_storefront.html', context)
        else:
            return redirect('vendor_signup')  
        
    else:
        
        return render(request, 'user_profile/other_storefront.html', context) 
        

def other_store(request, username):
    """ A view to return the users store """
    profile = get_object_or_404(UserProfile, user=username)
    products = Product.objects.all()
    username= username
    queries = Q(vendor__iexact=username)  
    products = products.filter(queries)
    product_number = products.count()

    context = {
        'products': products,
        'username': username,
        'product_number': product_number,
        'profile': profile,
    }

    if username == request.user.username:
        return render(request, 'user_profile/my_storefront.html', context) 
    else:
        return render(request, 'user_profile/other_storefront.html', context)         


# a view to render the purchased scores page
def purchased_scores(request):
    """ A view to return the purchased scores page """
    profile = get_object_or_404(UserProfile, user=request.user)
    products = Product.objects.all()
    orders = profile.orders.all()
    items = []
    score_number = 0

    for order in orders:
        for item in order.lineitems.all():
            items.append(item)
            score_number += 1
    
    

    context = {
        'products': products,
        'profile': profile,
        'orders': orders,
        'items': items,
        'score_number': score_number
        
    }

    return render(request, 'user_profile/purchased-scores.html', context)


def vendor_signup(request):
    """ A view to return the vendor signup page """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = vendorForm(request.POST)
        if form.is_valid():
            profile.sort_code = form.cleaned_data['sort_code']
            profile.account_number = form.cleaned_data['account_number']
            profile.card_name = form.cleaned_data['card_name']
            profile.vendor = True
            profile.save()    
            messages.success(request, 'Congratulations! You are now a vendor')   
            return redirect('storefront', storevendor=request.user.username)

    form = vendorForm()

    return render(request, 'user_profile/vendor-signup.html', {'form': form})

def edit_profile(request):
    """ Edit users profile information """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':

        form = UserProfileForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            if obj.profile_picture:
                obj.profile_picture = form.cleaned_data['profile_picture']
                obj.profile_picture.name = f"{request.user.username}-profile-picture.jpg"
            if obj.cover_photo:
                obj.cover_photo = form.cleaned_data['cover_photo']
                obj.cover_photo.name = f"{request.user.username}-cover-photo.jpg"    
            
            obj.sort_code = form.cleaned_data['sort_code']
            obj.account_number = form.cleaned_data['account_number']
            obj.card_name = form.cleaned_data['card_name']
            obj.save()
            
            
            return redirect('storefront', storevendor=request.user.username)
        else:
            messages.error(request, 'Failed to update profile. Please ensure the form is valid.')
    else:
        profile = get_object_or_404(UserProfile, user=request.user)

        form = UserProfileForm( instance=profile,initial={'sort_code': profile.sort_code, 'account_number': profile.account_number, 'card_name': profile.card_name, 'bio': profile.bio, 'profile_picture': profile.profile_picture, 'cover_photo': profile.cover_photo})
        template = 'user_profile/edit_profile.html'
    
    template = 'user_profile/edit_profile.html'
    
    context = {
        'form': form,
        'profile':profile
    }

    return render(request, template, context)    