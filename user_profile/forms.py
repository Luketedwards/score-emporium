from django import forms
from .models import UserProfile


class vendorForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['card_name', 'sort_code', 'account_number']
        labels = {
            'card_name': 'Name as it appears on your card',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['card_name'].help_text = 'Please enter the name as it appears on your card'
        self.fields['sort_code'].help_text = 'Please enter your sort code'
        self.fields['account_number'].help_text = 'Please enter your account number'

        # make all fields required
        for field in iter(self.fields):
            self.fields[field].required = True


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = [
            'profile_picture',
            'cover_photo',
            'card_name',
            'sort_code',
            'account_number',
            'bio']
        labels = {
            'profile_picture': 'Profile Picture',
            'cover_photo': 'Cover Photo'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['profile_picture'].help_text = 'Please upload a profile picture'
        self.fields['cover_photo'].help_text = 'Please upload a cover photo'

        # make fields required
        for field in iter(self.fields):
            self.fields['card_name'].required = True
            self.fields['sort_code'].required = True
            self.fields['account_number'].required = True
