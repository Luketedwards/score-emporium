from django import forms
from .models import ScoreRequest



class RequestForm(forms.ModelForm):
    model = ScoreRequest
    class Meta:
        model = ScoreRequest
        fields = ['title', 'description', 'video_link', 'link' ]
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        