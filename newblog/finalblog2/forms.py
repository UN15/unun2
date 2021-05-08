from django import forms
from .models import Finalblog2

class BlogForm(forms.ModelForm):
    class Meta:
        model = Finalblog2
        fields=['title', 'writer', 'body', 'image']