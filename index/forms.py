from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import LINK

class linkform(forms.Form):
    add_name = forms.CharField(label="Name")
    add_link = forms.CharField(label="Link")