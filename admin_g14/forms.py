from .models import *
from django import forms
from django.forms import ModelForm
from django.forms import DateTimeInput


class FormOrganization(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Organization
        fields = '__all__'
        labels = {
            'name': 'Organization Name',
        }

class FormUser(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'name': 'User Name',
        }

class FormLocation(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Location
        fields = '__all__'
        labels = {
            'name': 'Location Name',
            'address': 'Location Address',
        }

class FormWasteCat(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = WasteCat
        fields = '__all__'

class FormWasteItem(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = WasteItem
        fields = '__all__'

class FormWasteLog(ModelForm):
        required_css_class = 'required'
        class Meta:
            model = WasteLog
            fields = ['log_id','name','location','organization','waste_item','waste_quantity','datetime','created_by']
            widgets = {
            'datetime': DateTimeInput(attrs={'type': 'date'}),
            'waste_item': forms.SelectMultiple(attrs={'style': 'width: 500px;'}),
            'organization': forms.SelectMultiple(attrs={'style': 'width: 500px;'}),
            'location': forms.SelectMultiple(attrs={'style': 'width: 500px;'})
            }
            labels = {
            'name': 'Description',
            'waste_quantity' : 'Quantity Wasted (in Kg)',
            'datetime' : ' Date',
            'created_by' : 'Who am I'
        }

