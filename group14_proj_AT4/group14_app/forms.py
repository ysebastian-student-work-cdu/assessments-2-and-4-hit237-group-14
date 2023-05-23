from django import forms
from django.forms import ModelForm
from .models import Contact, WasteLog

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input','placeholder':'Full Name', 'style': 'height:30px; width:100%;'}),
            'email': forms.EmailInput(attrs={'class': 'form-input','placeholder':'Email Address', 'style':' height:30px; width:100%;'}),
            'subject': forms.TextInput(attrs={'class': 'form-input','placeholder':'Subject', 'style':' height:30px; width:100%;'}),
            'message': forms.Textarea(attrs={'class': 'form-input','rows':5, 'placeholder':'Tell us what we can help you with', 'style': 'height:80px; width:100%;'}),
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