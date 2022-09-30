from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from products.models import Product
from .models import UserProfile
from .forms import vendorForm, UserProfileForm
from django.contrib import messages
import datetime


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
        user2 = get_object_or_404(User, username=storevendor)

        profile = get_object_or_404(UserProfile, user=user2)
    orders = profile.orders.all()

    vendor_profile = profile
    # get all products
    vendor_products = Product.objects.all()
    vendor_average_rating = 0
    reviewed_products = 0
    try:
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
    except BaseException:
        vendor_average_rating = 0

    if request.user.is_authenticated:

        orders2 = profile.orders.all()

    else:
        orders2 = None

    ordersList = []
    if request.user.is_authenticated:
        for order in orders2:
            for item in order.lineitems.all():
                ordersList.append(item.product.id)

    products = Product.objects.all()
    all_products = products
    username = request.user.username
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
        'sales_number': sales_number,
        'sales_income': sales_income,
        'money_due': money_due,
        'storevendor': storevendor,
        'ordersList': ordersList,
        'vendor_average_rating': vendor_average_rating,

    }

    if username == storevendor:
        if profile.vendor:
            return render(request, 'user_profile/my_storefront.html', context)
        else:
            return redirect('vendor_signup')

    else:

        return render(request, 'user_profile/other_storefront.html', context)


def other_store(request, username):
    """ A view to return the users store """
    profile = get_object_or_404(UserProfile, user=username)
    products = Product.objects.all()
    username = username
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

        form = UserProfileForm(request.POST, request.FILES, instance=profile)
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
            messages.error(
                request,
                'Failed to update profile. Please ensure the form is valid.')
    else:
        profile = get_object_or_404(UserProfile, user=request.user)

        form = UserProfileForm(
            instance=profile,
            initial={
                'sort_code': profile.sort_code,
                'account_number': profile.account_number,
                'card_name': profile.card_name,
                'bio': profile.bio,
                'profile_picture': profile.profile_picture,
                'cover_photo': profile.cover_photo})
        template = 'user_profile/edit_profile.html'

    template = 'user_profile/edit_profile.html'

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, template, context)


def dashboard(request):
    """ A view to return the dashboard page """
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        if profile.vendor:

            """ A view to return the dashboard page """
            profile = get_object_or_404(UserProfile, user=request.user)
            products = Product.objects.all()
            orders = profile.orders.all()
            items = []
            number_of_customers = orders.distinct('username').count()
            number_of_orders = orders.count()
            total_revenue = 0
            for order in orders:
                total_revenue += order.order_total
            total_revenue = float(total_revenue) * 0.8

            # find orders placed today
            today = datetime.date.today()
            today_total = 0
            orders_today = orders.filter(
                date__day=today.day,
                date__month=today.month,
                date__year=today.year)
            for order in orders_today:
                today_total += order.order_total
            today_total = float(today_total) * 0.8

            # find orders placed this week
            week_total = 0
            orders_week = orders.filter(date__week=today.isocalendar()[1])
            for order in orders_week:
                week_total += order.order_total
            week_total = float(week_total) * 0.8

            # find orders placed last week
            last_week_total = 0
            orders_last_week = orders.filter(
                date__week=today.isocalendar()[1] - 1)
            for order in orders_last_week:
                last_week_total += order.order_total
            last_week_total = float(last_week_total) * 0.8

            # calculate the percentage difference between this week and last
            # week
            if last_week_total == 0:
                week_difference = 100
            else:
                week_difference = (
                    week_total - last_week_total) / last_week_total * 100

            # find orders placed this month
            month_total = 0
            orders_month = orders.filter(date__month=today.month)
            for order in orders_month:
                month_total += order.order_total
            month_total = float(month_total) * 0.8

            # find distinct products in orders
            distinct_products = []
            for order in orders:
                for item in order.lineitems.all():
                    distinct_products.append(item.product.id)
            distinct_products = set(distinct_products)

            # calculate the number of orders this week
            orders_this_week = orders.filter(date__week=today.isocalendar()[1])
            orders_this_week = orders_this_week.count()

            # calculate the number of orders last week
            orders_last_week = orders.filter(
                date__week=today.isocalendar()[1] - 1)
            orders_last_week = orders_last_week.count()

            # calculate the number of orders this month
            orders_this_month = orders.filter(date__month=today.month)
            orders_this_month = orders_this_month.count()

            # calculate the percentage difference between this week and last
            # week
            if orders_last_week == 0:
                orders_week_difference = 100
            else:
                orders_week_difference = (
                    orders_this_week - orders_last_week) / orders_last_week * 100

            # calculate number of distinct customers this week
            customer_orders_this_week = orders.filter(
                date__week=today.isocalendar()[1])
            customers_this_week = customer_orders_this_week.distinct(
                'username').count()

            # calculate number of distinct customers last week
            customer_orders_last_week = orders.filter(
                date__week=today.isocalendar()[1] - 1)
            customers_last_week = customer_orders_last_week.distinct(
                'username').count()

            # calculate the percentage difference between this week and last
            # week
            if customers_last_week == 0:
                customers_week_difference = 100
            else:
                customers_week_difference = (
                    customers_this_week - customers_last_week) / customers_last_week * 100

        # order distinct products by number sold
            product_sales = []
            for product in distinct_products:
                product_sales.append(
                    (product, orders.filter(
                        lineitems__product=product).count()))
            product_sales.sort(key=lambda x: x[1], reverse=True)
            product_sales = product_sales[:5]

            # filter products by product_sales
            top_products = []
            for product in product_sales:
                top_products.append(Product.objects.get(id=product[0]))

            # create dictionary of top products and their sales
            top_products_dict = {}
            for product in top_products:
                top_products_dict[product] = orders.filter(
                    lineitems__product=product).count()

            # calculate total revenue for each product in top_products and make
            # a dictionary
            top_products_revenue = {}
            for product in top_products:
                total = 0
                for order in orders.filter(lineitems__product=product):
                    total += order.order_total
                top_products_revenue[product] = float(total) * 0.8

            # find genre of all products sold in orders
            genres = []
            for order in orders:
                for item in order.lineitems.all():
                    genres.append(item.product.genre)
            genres = set(genres)

            # find most popular genre
            try:
                genre_sales = []
                for genre in genres:
                    genre_sales.append(
                        (genre, orders.filter(
                            lineitems__product__genre=genre).count()))
                genre_sales.sort(key=lambda x: x[1], reverse=True)
                genre_sales = genre_sales[:5]
                most_popular_genre = genre_sales[0][0]
            except BaseException:
                most_popular_genre = 'N/A'

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
                'score_number': score_number,
                'number_of_customers': number_of_customers,
                'number_of_orders': number_of_orders,
                'total_revenue': total_revenue,
                'today_total': today_total,
                'week_total': week_total,
                'month_total': month_total,
                'distinct_products': distinct_products,
                'product_sales': product_sales,
                'top_products': top_products,
                'top_products_dict': top_products_dict,
                'top_products_revenue': top_products_revenue,
                'week_difference': week_difference,
                'orders_week_difference': orders_week_difference,
                'orders_this_week': orders_this_week,
                'orders_last_week': orders_last_week,
                'orders_this_month': orders_this_month,
                'customers_week_difference': customers_week_difference,
                'most_popular_genre': most_popular_genre,

            }
            if number_of_customers == 0:
                # if there are no customers, redirect to empty dashboard
                return render(
                    request,
                    'user_profile/dashboard-empty.html',
                    context)
            else:
                return render(request, 'user_profile/dashboard.html', context)
        else:
            messages.error(request, 'You must be a vendor to access this page')
            return redirect('vendor_signup')
    else:
        return redirect('account_signup')
