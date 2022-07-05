from django.shortcuts import render

# Create your views here.

def user_profile(request):
    """ A view to return the index page """

    return render(request, 'user_profile/profile.html')