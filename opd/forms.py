from django import forms
from django.forms import ModelForm
from .models import Country


class Country_Form(forms.ModelForm):

    class Meta:
        model = Country
        fields = ['country_name']
