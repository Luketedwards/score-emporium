from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import RequestForm, CommentForm, SubmissionForm
from .models import ScoreRequest, Comments, ScoreSubmissions
from django.core.files.storage import FileSystemStorage

# Create your views here.


def requests(request):
    """ A view to return the requests page """
    form = CommentForm
    form2 = SubmissionForm
    # get all distinct requests and order by 'liked'
    requests = ScoreRequest.objects.distinct().order_by('liked')
    submissions = ScoreSubmissions.objects.all().order_by('-date')
    active_submissions = ScoreRequest.objects.distinct().filter(completed=False).count()
    inactive_submissions = ScoreRequest.objects.distinct().filter(completed=True).count()
    comments = Comments.objects.all()
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
        if requested.liked.filter(id=request.user.id).exists():
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
        'active_submissions': active_submissions,
        'inactive_submissions': inactive_submissions,

    }

    return render(request, 'voting/requests2.html', context)


def completed_requests(request):
    """ A view to return the completed requests page """
    form = CommentForm
    form2 = SubmissionForm
    requests = ScoreRequest.objects.all().order_by('liked')
    submissions = ScoreSubmissions.objects.all().order_by('-date')
    inactive_submissions = ScoreRequest.objects.filter(completed=True).count()

    comments = Comments.objects.all()
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
        if requested.liked.filter(id=request.user.id).exists():
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
        'inactive_submissions': inactive_submissions,


    }
    return render(request, 'voting/completed_requests.html', context)


# render the make request page
def make_request(request):
    """ A view to return the make request page """
    user = request.user
    if user.is_authenticated:
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
                messages.error(
                    request, 'Failed to add request. Please ensure the form is valid.')
        else:
            form = RequestForm()
            template = 'voting/make-a-request.html'

        context = {
            'form': form,
        }

        return render(request, template, context)
    else:
        messages.error(
            request,
            'You must be logged in to make a score request.')
        return redirect('account_login')


def create_submission(request, pk):
    """ A view to return the create submission page """
    post = get_object_or_404(ScoreRequest, pk=pk)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        folder = 'media/submissions/'
        if form.is_valid():

            submission = form.save(commit=False)
            submission.score = post
            submission.created_by = request.user

            if submission.PDF:
                # rename the pdf file to created_by and the post's title
                myfile = request.FILES['PDF']
                fs = FileSystemStorage(
                    location=folder)  # defaults to   MEDIA_ROOT
                fs.save(
                    f'submission_request_{request.user.username}_{post.title}.pdf',
                    myfile)
                submission.PDFpath = f'media/submissions/submission_request_{request.user.username}_{post.title}.pdf'

            messages.success(request, f"pdf detected")

            submission.save()
            messages.success(
                request, f"Successfully submitted to {post.title}!")
            return redirect('requests')
    else:
        messages.error(
            request,
            'Failed to add submission. Please ensure the form is valid.')
        return redirect('requests')

    return redirect('requests')


def delete_post(request, pk):
    """ A view to delete a post """
    post = get_object_or_404(ScoreRequest, pk=pk)
    if request.user == post.created_by:
        post.delete()
        messages.success(request, f"Successfully deleted {post.title}!")

        return redirect('requests')
    return render(request, 'voting/requests.html')


def like_post(request, pk):
    """ A view to like a post """
    post = get_object_or_404(ScoreRequest, pk=pk)
    liked = False
    if post.liked.filter(id=request.user.id).exists():
        post.liked.remove(request.user)
        post.upvotes -= 1
        post.save()

        return redirect('requests')

    else:
        post.upvotes += 1
        post.liked.add(request.user)
        post.save()

        return redirect('requests')
    return render(request, 'voting/requests.html')


def like_post_completed(request, pk):
    """ A view to like a post on a completed request page """
    post = get_object_or_404(ScoreRequest, pk=pk)
    liked = False
    if post.liked.filter(id=request.user.id).exists():
        post.liked.remove(request.user)
        post.upvotes -= 1
        post.save()

        return redirect('completed_requests')

    else:
        post.upvotes += 1
        post.liked.add(request.user)
        post.save()

        return redirect('completed_requests')
    return render(request, 'voting/requests.html')


def comment_post(request, pk):
    """ A view to comment on a post """
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


def comment_post_completed(request, pk):
    """ A view to comment on a post on a completed request page """
    post = get_object_or_404(ScoreRequest, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.score = post
            comment.created_by = request.user
            comment.save()
            return redirect('completed_requests')
    else:
        form = CommentForm()
    return render(request, 'voting/comment.html', {'form': form})


def dislike_post(request, pk):
    """ A view to dislike a post """
    post = get_object_or_404(ScoreRequest, pk=pk)
    if request.method == 'POST':
        post.upvotes -= 1
        post.likes.remove(request.user)
        post.save()
        return redirect('requests')
    return render(request, 'voting/requests.html')


def dislike_post_completed(request, pk):
    """ A view to dislike a post on a completed request page """
    post = get_object_or_404(ScoreRequest, pk=pk)
    if request.method == 'POST':
        post.upvotes -= 1
        post.likes.remove(request.user)
        post.save()
        return redirect('completed_requests')
    return render(request, 'voting/requests.html')


def accept_score_submission(request, pk, score_pk):
    """ A view to accept a score submission """
    post = get_object_or_404(ScoreSubmissions, pk=pk)
    score = get_object_or_404(ScoreRequest, pk=score_pk)
    score.completed = True
    score.save()
    post.accepted = True
    post.save()
    messages.success(request, f"Successfully accepted {post.PDF}!")
    return redirect('requests')

def decline_score_submission(request, pk):
    """ A view to decline score submission"""
    # get submission
    post = get_object_or_404(ScoreSubmissions, pk=pk)
    # delete submission
    post.delete()
    messages.success(request, f"Successfully declined!")
    return redirect('requests')

        
