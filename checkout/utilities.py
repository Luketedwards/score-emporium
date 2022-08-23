
from __future__ import print_function
from django.conf import settings

from django.shortcuts import get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

from score_emporium.settings import SENDBLUE_PASSWORD


from .models import Order




def notify_vendor(order):
    
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = SENDBLUE_PASSWORD
    
    
    from_email = settings.DEFAULT_EMAIL_FROM
    order_number = order.order_number
    order = get_object_or_404(Order, order_number=order_number)

    for vendor in order.lineitems.all():
        
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
        subject = "New Order!"
        sender = {"name":"noreply@scoreemporium.com","email":"scoreemporium@gmail.com"}
        reply_to = {"name":"noreply@scoreemporium.com","email":"scoreemporium@gmail.com"}

        html_content = render_to_string('checkout/notify_vendor.html', {'order': order, 'vendor': vendor.product.vendor})
        to = [{"email":"luketedmusic@gmail.com","name":"Luke"}]
        
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
    