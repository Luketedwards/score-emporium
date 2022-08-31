
from django.shortcuts import render, get_object_or_404
from products.models import Review
import random
# Create your views here.

def index(request):
    """ A view to return the index page """
    reviews = Review.objects.all().order_by('-ratings')
    reviews = reviews[:3]
    review1 = reviews[random.randint(0, len(reviews) - 1)]
    review2 = reviews[random.randint(0, len(reviews) - 1)]
    number1 = random.randint(0, len(reviews) - 1)
    number2 = random.randint(0, len(reviews) - 1)
    
    context = {
        'review1': review1,
        'review2': review2,
        'number1': number1,
        'number2': number2,
        'reviews': reviews
    }

    return render(request, 'home/index.html' , context)