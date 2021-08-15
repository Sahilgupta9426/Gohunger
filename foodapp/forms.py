from django.core import validators
from django import forms
from django.forms import fields, widgets
from .models import Contact,Menu



class ContactReg(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','number','details']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'number':forms.TextInput(attrs={'class':'form-control'}),
            'details':forms.TextInput(attrs={'class':'form-control'}),
            
            }
