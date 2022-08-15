from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.contrib import messages

from .forms import RequestForm

from .models import ScoreRequest

# Create your views here.

# renders the requests page
def requests(request):
    requests = ScoreRequest.objects.all()

    if request.method == 'POST':
        
        current_request = ScoreRequest.objects.get(id=request.POST['id'])
        
        if request.user in current_request.like_list.all():
            current_request.like_list.remove(request.user)
            current_request.upvotes -= 1
            current_request.save()
            thumbup = True

        else:    
            current_request.upvotes += 1
            
            current_request.like_list.add(request.user)
            current_request.save()
            thumbup = False


        context = {
            'requests': requests,
            'thumbup': thumbup,
        }
        return redirect(reverse('requests'), context)

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
            context = {
            'requests': requests,
            }
            return render(request, 'voting/requests.html',context)

        else:
            messages.error(request, 'Failed to add request. Please ensure the form is valid.')
    else:
        form = RequestForm()
        template = 'voting/make-a-request.html'
        

    context = {
        'form': form,
    }

    return render(request, template, context)
    
    