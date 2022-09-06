from django import forms
from .models import ScoreRequest, Comments, ScoreSubmissions




class RequestForm(forms.ModelForm):
    model = ScoreRequest
    class Meta:
        model = ScoreRequest
        fields = ['title', 'description', 'video_link', 'link' ]
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CommentForm(forms.ModelForm):
    model = Comments
    class Meta:
        model = Comments
        fields = ['content' ]
        labels = {
            'content': 'Comments',
        }
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class SubmissionForm(forms.ModelForm):
    model = ScoreSubmissions
    class Meta:
        model = ScoreSubmissions
        fields = ['content', 'link', 'PDF' ]
        
        labels = {
            'content': 'Message',
            'link': 'Link to Product',
        }
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   