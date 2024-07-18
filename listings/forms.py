from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'category', 'image']

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search Categories')