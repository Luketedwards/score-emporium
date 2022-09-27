
from django.shortcuts import render
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
