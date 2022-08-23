from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from user_profile.models import UserProfile
from cart.contexts import cart_contents

import stripe

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        vendors = {}
        
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'username': request.user.username,
            'quantity': 1,
            
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                
                try:
                    #Add item to users purchased scores
                    

                    product = Product.objects.get(id=item_id)
                    
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            
                        )
                        order_line_item.save()

                        # connects sales data to user profile
                        
                        userId = get_object_or_404(User,username=order_line_item.product.vendor)
                        comission_value = float(order_line_item.product.price) * 0.8
                        vendor = UserProfile.objects.get(user=userId)
                        vendor.sales_number = vendor.sales_number + 1
                        vendor.sales_income = vendor.sales_income + int(comission_value)
                        sale = {
                            'vendor': vendor,
                            'product': product,
                            'sale_value': comission_value,
                        }
                        vendors.append(sale)
                        vendor.save()
                        
                        
                    
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the items in your cart is no longer available.")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))
                
            request.session['save_info'] = 'save-info' in request.POST



            for vendor in order.vendors:
                if vendor not in vendors:
                    vendors.append(vendor)

            for product in order.products:
                vendors[str(product.vendor)].append(product)
                vendors[str(product.vendor)].append(product.price)
                
           
            # send email to vendor with order details
            for vendor in vendors:
                send_mail(
                    'You have a new order!',
                    'Hello {{vendor.user.username}}! You have a new order! The details are as follows:\
                        Order number:{{order.order_number}}. \
                        Date:{{order.date}}. \
                        Customer Name:{{order.full_name}}. \
                        Items: {% for items in vendors.product %} {% if item.vendor == vendor %} {{vendor.product.name}}. {%endif%} {%endfor%} \
                        Total: {{vendor.sale_value}}. \
                        Congratulations on your new sale!',
                    'luketedmusic@gmail.com',
                    ['{{vendor.user.email}}'],
                    fail_silently=False,
                )

            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is currently empty.")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

            

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    
    save_info = request.session.get('save_info')
    
    order = get_object_or_404(Order, order_number=order_number)
    

    profile = UserProfile.objects.get(user=request.user)
    # Attach the user's profile to the order
    order.user_profile = profile
    order.save()
    
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')


    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    
    return render(request, template, context)    