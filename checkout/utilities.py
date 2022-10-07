
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


def notify_vendor2(vendorName, order):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = SENDBLUE_PASSWORD
    order_total = order.order_total

    from_email = settings.DEFAULT_EMAIL_FROM
    order_number = order.order_number

    # find all orders made by vendor
    vendor_orders = Order.objects.filter(lineitems__vendor=vendorName)
    # count the number of orders made by vendor
    vendor_orders_count = vendor_orders.count()

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration))

    subject = "New Order!"
    sender = {
        "name": "noreply@scoreemporium.com",
        "email": "scoreemporium@gmail.com"}
    reply_to = {
        "name": "noreply@scoreemporium.com",
        "email": "scoreemporium@gmail.com"}
    profile = get_object_or_404(User, username=vendorName)
    vendors_total = 0
    pre_comission_total = 0

    for item in order.lineitems.all():
        if item.vendor == vendorName:
            price = float(item.product.price)
            price2 = float(item.product.price)
            price = price * 0.8
            vendors_total = vendors_total + price
            pre_comission_total = pre_comission_total + price2

    html_content = render_to_string(
        'checkout/notify_vendor_email.html',
        {
            'order': order,
            'vendor': vendorName,
            'vendors_total': vendors_total,
            'pre_comissions': pre_comission_total,
            'vendor_orders_count': vendor_orders_count,
            'order_total': order_total})
    to = [{"email": profile.email, "name": vendorName}]

    params = {"parameter": "My param value", "subject": "New Subject"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        reply_to=reply_to,
        html_content=html_content,
        sender=sender,
        subject=subject)
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)


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

            api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
                sib_api_v3_sdk.ApiClient(configuration))
            subject = "New Order!"
            sender = {
                "name": "noreply@scoreemporium.com",
                "email": "scoreemporium@gmail.com"}
            reply_to = {
                "name": "noreply@scoreemporium.com",
                "email": "scoreemporium@gmail.com"}
            profile = get_object_or_404(User, username=vendor.vendor)
            vendors_total = 0
            for item in order.lineitems.all():
                if item.vendor == vendor.vendor:
                    price = float(item.product.price)
                    price = price * 0.8
                    vendors_total = vendors_total + price
            html_content = render_to_string(
                'checkout/notify_vendor_email.html',
                {
                    'order': order,
                    'vendor': vendor.vendor,
                    'vendors_total': vendors_total})
            to = [{"email": profile.email, "name": vendor.vendor}]

            params = {"parameter": "My param value", "subject": "New Subject"}
            send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
                to=to,
                reply_to=reply_to,
                html_content=html_content,
                sender=sender,
                subject=subject)
        try:
            api_response = api_instance.send_transac_email(send_smtp_email)
            print(api_response)
        except ApiException as e:
            print(
                "Exception when calling SMTPApi->send_transac_email: %s\n" %
                e)


def notify_customer(order):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = SENDBLUE_PASSWORD
    order_total = order.order_total
    from_email = settings.DEFAULT_EMAIL_FROM
    order_number = order.order_number

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration))

    subject = "Your Order Details!"
    sender = {
        "name": "noreply@scoreemporium.com",
        "email": "scoreemporium@gmail.com"}
    reply_to = {
        "name": "noreply@scoreemporium.com",
        "email": "scoreemporium@gmail.com"}

    total_price = 0
    for item in order.lineitems.all():

        price = float(item.product.price)
        total_price = total_price + price

    html_content = render_to_string(
        'checkout/notify_customer_email.html', {'order': order, 'total_price': total_price, 'order_total': order_total})
    to = [{"email": order.email, "name": order.full_name}]

    params = {"parameter": "My param value", "subject": "New Subject"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        reply_to=reply_to,
        html_content=html_content,
        sender=sender,
        subject=subject)
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
