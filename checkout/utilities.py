from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string



from .models import Order



def notify_vendor(order):
    from_email = settings.DEFAULT_EMAIL_FROM
    order_number = order.order_number
    order = get_object_or_404(Order, order_number=order_number)

    for vendor in order.lineitems.all():
        
        to_email = 'luketedmusic@gmail.com'
        subject = 'New order'
        text_content = 'You have a new order!'
        html_content = render_to_string('checkout/notify_vendor.html', {'order': order, 'vendor': vendor.product.vendor})
        send_mail(subject, html_content, from_email, [to_email])
        

def notify_customer(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    to_email = order.email
    subject = 'Order confirmation'
    text_content = 'Thank you for the order!'
    html_content = render_to_string('checkout/notify_customer.html', {'order': order})

    send_mail(subject, html_content, from_email, [to_email])
    