from .models import *
from django import forms
from django.forms import ModelForm
from django.forms import DateTimeInput


class FormOrganization(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Organization
        fields = '__all__'

class FormUser(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = User
        fields = '__all__'

class FormLocation(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Location
        fields = '__all__'

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
            'waste_item': forms.Select(attrs={'style': 'width: 500px;'}),
            'organization': forms.Select(attrs={'style': 'width: 500px;'}),
            'location': forms.Select(attrs={'style': 'width: 500px;'})
            }
