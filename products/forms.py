from django import forms
from .models import Product, Genre


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'genre', 'difficulty', 'description', 'price', 'image', 'PDF', 'Guitar_Pro', 'video' ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in genres]

        self.fields['genre'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'