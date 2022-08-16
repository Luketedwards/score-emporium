from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.contrib import messages

from .forms import RequestForm, CommentForm

from .models import ScoreRequest, Comment

# Create your views here.

# renders the requests page
def requests(request):
    form = CommentForm
    requests = ScoreRequest.objects.all()
    comments = Comment.objects.all()
    list = []

    for requested in requests:
        if requested.likes.filter(id=request.user.id).exists():
            list.append(requested.pk)
            
    
    user = request.user
    
    
    context = {
        'requests': requests,
        'user': user,
        'comments': comments,
        'list': list,
        'form': form,

    }
    return render(request, 'voting/requests.html',context)


# render the make request page
def make_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form:
            obj = form.save(commit=False)

            obj.created_by = request.user
            
            obj.save()
                            
            messages.success(request, 'Successfully added request!')
            context = {
            'requests': requests,
            }
            return redirect('requests')


        else:
            messages.error(request, 'Failed to add request. Please ensure the form is valid.')
    else:
        form = RequestForm()
        template = 'voting/make-a-request.html'
        

    context = {
        'form': form,
    }

    return render(request, template, context)
    

def like_post(request, pk):
    post = get_object_or_404(ScoreRequest, pk=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        post.upvotes -= 1
        post.save()
        
        return redirect('requests')

    else:    
        post.upvotes += 1
        post.likes.add(request.user)
        post.save()
        
        return redirect('requests')
    return render(request, 'voting/requests.html')

def comment_post(request, pk):
    post = get_object_or_404(ScoreRequest, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.score = post
            comment.created_by = request.user
            comment.save()
            return redirect('requests')
    else:
        form = CommentForm()
    return render(request, 'voting/comment.html', {'form': form})

def dislike_post(request, pk):
    post = get_object_or_404(ScoreRequest, pk=pk)
    if request.method == 'POST':
        post.upvotes -= 1
        post.likes.remove(request.user)
        post.save()
        return redirect('requests')
    return render(request, 'voting/requests.html')    
    