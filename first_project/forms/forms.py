from django import forms
from django.core import validators

class FormName(forms.Form):
	name = forms.CharField(label='Your Name',max_length=100)
	email = forms.CharField()
	botcatcher = forms.CharField(required=False,
								widget=forms.HiddenInput,
								validators=[validators.MaxLengthValidator(0)])

