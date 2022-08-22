from email import message
from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.contrib import messages

from .forms import RequestForm, CommentForm, SubmissionForm

from .models import ScoreRequest, Comment, ScoreSubmissions

# Create your views here.

# renders the requests page
def requests(request):
    form = CommentForm
    form2 = SubmissionForm
    requests = ScoreRequest.objects.all().order_by('-likes')
    submissions = ScoreSubmissions.objects.all().order_by('-date')
    comments = Comment.objects.all()
    list = []
    comment_list = []

    for score in requests:
        
        relevant_comments = comments.filter(score=score)
        
        count = relevant_comments.count()
        joined = {
            'score': score.id,
            'commentCount': count,
        }
        comment_list.append(joined)
        

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
        'comment_list': comment_list,
        'form2': form2,
        'submissions': submissions,

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
    

def create_submission(request, pk):
    post = get_object_or_404(ScoreRequest, pk=pk)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.score = post
            submission.created_by = request.user
            submission.PDF = request.POST['PDF']
            if submission.PDF:
                # rename the pdf file to created_by and the post's title
                submission.PDF.name = f'submission_request_{request.user.username}_{post.title}.pdf'

                
            submission.save()
            messages.success(request, f"Successfully submitted to {post.title}!")
            return redirect('requests')
    else:
        messages.error(request, 'Failed to add submission. Please ensure the form is valid.')
        return redirect('requests')

    return redirect('requests')


def delete_post(request, pk):
    post = get_object_or_404(ScoreRequest, pk=pk)
    if request.user == post.created_by:
        post.delete()
        messages.success(request, f"Successfully deleted {post.title}!")
        
        return redirect('requests')
    return render(request, 'voting/requests.html')    

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
    
# accepts submission to the score and marks it as accepted
def accept_score_submission(request, pk):
    post = get_object_or_404(ScoreSubmissions, pk=pk)
    
    post.accepted = True
    post.save()
    messages.success(request, f"Successfully accepted {post.PDF}!")
    return redirect('requests')
    



