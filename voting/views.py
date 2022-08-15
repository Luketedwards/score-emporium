from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.contrib import messages

from .forms import RequestForm

from .models import ScoreRequest

# Create your views here.

# renders the requests page
def requests(request):
    requests = ScoreRequest.objects.all()

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            post = request.POST('id')
            post.upvotes += 1
            user = request.user
            post.like_list.add(user)
            post.save()
            return redirect(reverse('requests'))

    context = {
        'requests': requests,
    }
    return render(request, 'voting/requests.html',context)


# render the make request page
def make_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form:
            form.created_by = request.user
            form.save()
                            
            messages.success(request, 'Successfully added request!')
            return redirect(reverse('requests'))
        else:
            messages.error(request, 'Failed to add request. Please ensure the form is valid.')
    else:
        form = RequestForm()
        template = 'voting/make-a-request.html'
        

    context = {
        'form': form,
    }

    return render(request, template, context)
    
    