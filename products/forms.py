from django import forms
from .models import Product, Genre


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'genre', 'difficulty', 'description', 'price', 'image', 'PDF', 'Guitar_Pro_Unlocked', 'Guitar_Pro_Locked', 'video' ]
        labels = {
            'name': 'Score Name',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in genres]
        self.fields['video'].help_text = 'Please use the Youtube "embed" option, and not the "watch link".'
        self.fields['Guitar_Pro_Unlocked'].help_text = 'This file will be used to play in the browser. Ensure the file is not locked or it will fail to work..'
        self.fields['Guitar_Pro_Locked'].help_text = 'This file will be distributed to the customer for download. We recommend locking the file to prevent changes being made.<strong>You may also upload an unlocked file if you wish.</strong>'

        self.fields['genre'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'