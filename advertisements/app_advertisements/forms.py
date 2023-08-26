from django import forms
from django.forms import ModelForm
from .models import Advertisement
from django.core.exceptions import ValidationError

class AdvertisementForm2(ModelForm):
    
    title = forms.CharField(max_length=64,
                             widget=forms.TextInput(attrs={'class' : 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    auction = forms.BooleanField(required = False, widget=forms.CheckboxInput(attrs={'class' : 'form-check_input'}))
    image = forms.ImageField( widget=forms.FileInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
