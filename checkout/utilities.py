
from __future__ import print_function
from itertools import product
from django.conf import settings
from django.contrib.auth.models import User


from django.shortcuts import get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

from score_emporium.settings import SENDBLUE_PASSWORD


from .models import Order




def notify_vendor(vendorName, order):
    
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = SENDBLUE_PASSWORD
    
    
    from_email = settings.DEFAULT_EMAIL_FROM
    order_number = order.order_number
    order = get_object_or_404(Order, order_number=order_number)
    vendor_count = order.lineitems.values('vendor').distinct().count()

                                        
    count = 0
    while count < vendor_count:
        count = count + 1
        for vendor in order.lineitems.all():
            
                
            api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
            subject = "New Order!"
            sender = {"name":"noreply@scoreemporium.com","email":"scoreemporium@gmail.com"}
            reply_to = {"name":"noreply@scoreemporium.com","email":"scoreemporium@gmail.com"}
            profile = get_object_or_404(User, username=vendor.vendor)
            vendors_total = 0
            for item in order.lineitems.all():
                if item.vendor == vendor.vendor:
                    price = float(item.product.price) 
                    price = price * 0.8
                    vendors_total = vendors_total + price
            html_content = render_to_string('checkout/notify_vendor_email.html', {'order': order, 'vendor': vendor.vendor, 'vendors_total': vendors_total})
            to = [{"email": profile.email,"name":vendor.vendor}]
            
            params = {"parameter":"My param value","subject":"New Subject"}
            send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, reply_to=reply_to, html_content=html_content, sender=sender, subject=subject)
        try:
            api_response = api_instance.send_transac_email(send_smtp_email)
            print(api_response)
        except ApiException as e:
            print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
        

def notify_customer(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    to_email = order.email
    subject = 'Order confirmation'
    text_content = 'Thank you for the order!'
    html_content = render_to_string('checkout/notify_customer.html', {'order': order})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    