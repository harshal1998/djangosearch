from django import forms
from .models import *


class dform(forms.ModelForm):
    fname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'}), required=True, max_length=50)

    lname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name'}), required=True, max_length=50)

    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter City'}), required=True, max_length=50)

    class Meta:
        model = form
        fields = "__all__"
