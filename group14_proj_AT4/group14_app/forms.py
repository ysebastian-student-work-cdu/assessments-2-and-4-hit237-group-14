from django import forms
from django.forms import ModelForm
from .models import Contact, WasteLog

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

class LogForm(ModelForm):
    class Meta:
        model = WasteLog
        fields = '__all__'
        labels = {
            'organisation': 'Company or Organisation',
            'fullname': 'Full Name',
            'wastetype': 'Type of Waste',
            'foodname': 'Food Name',
            'date': 'Date of Disposal',
            'reason': 'Loss Reason',
            'measurement': 'How is it measured?',
            'foodsize': 'Food Size',
            'recorded': 'Recorded By'
        }
        widgets = {
            'organisation': forms.TextInput(attrs={'placeholder':'Your Organisation or Company'}),
            'fullname': forms.TextInput(attrs={'placeholder':'Your Full Name'}),
            'foodname': forms.TextInput(attrs={'placeholder':'Name of the food'}),
            'date': forms.TextInput(attrs={'placeholder':'eg. 26/07/2019'}),
            'reason': forms.TextInput(attrs={'placeholder':'Why is it thrown away?'}),
            'foodsize': forms.TextInput(attrs={'placeholder':'The size of the food'}),
            'recorded': forms.TextInput(attrs={'placeholder':'Who is this log recorded by?'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(LogForm,self).__init__(*args, **kwargs)
        self.fields['wastetype'].empty_label = "Select"
        self.fields['measurement'].empty_label = "Select"