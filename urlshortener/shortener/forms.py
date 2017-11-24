"""Form for urlshortener."""
from django import forms

from .models import Urls

class UrlsForm(forms.ModelForm):
    """Generate form from the model."""

    class Meta:
        """Have a single field `long_url` on the form."""

        model = Urls
        fields = ['long_url',]
