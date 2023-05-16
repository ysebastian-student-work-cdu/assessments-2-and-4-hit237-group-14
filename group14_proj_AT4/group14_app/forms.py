from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        labels = {
            'name': '',
            'email': '',
            'subject': '',
            'message': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email Address'}),
            'subject': forms.TextInput(attrs={'placeholder':'Subject'}),
            'message': forms.Textarea(attrs={'rows':5, 'placeholder':'Message'}),
        }