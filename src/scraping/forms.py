from django import forms

from scraping.models import City, Language

class FindForm(forms.Form):
    #If we add like a field name slug , then we need to change that field for home viev function in view.py
    # requered = if field empty also get request in form
    # Widgets - helps us to change default view of form fields, in our example we use bootstrap form-control class
    # Use label for change name of inputs
    city = forms.ModelChoiceField(queryset = City.objects.all(), to_field_name="slug", required=False, 
    widget=forms.Select(attrs={'class': 'form-control'}), label='City'
    )
    language = forms.ModelChoiceField(queryset = Language.objects.all(), to_field_name="slug", required=False,
    widget=forms.Select(attrs={'class': 'form-control'}), label='Major'
    )