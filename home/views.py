from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from products.models import Review
# Create your views here.


def index(request):
    """ A view to return the index page """
    reviews = Review.objects.all().order_by('-ratings')
    reviews = reviews[:6]

    context = {

        'reviews': reviews
    }

    return render(request, 'home/index.html', context)

def newsletter(request):
    """ A view to return the newsletter page """
    # refresh the page the user posted from
    if request.method == 'POST':
        messages.success(request, 'You have successfully subscribed to our newsletter!')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(reverse('home'))
