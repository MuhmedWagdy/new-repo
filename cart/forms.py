from django import forms
from django.forms.widgets import Widget


CHOICES = [(i, str(i)) for i in range(1, 21)]


class ProductAddForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=CHOICES, coerce=int)
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput)
