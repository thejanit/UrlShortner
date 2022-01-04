from django import forms
from django import forms

class Shortened_Form(forms.Form):
    original_url = forms.URLField(widget=forms.URLInput(attrs={
        "class": "form-control form-control-lg", "placeholder": "Type your url for shorten..."
    }))
