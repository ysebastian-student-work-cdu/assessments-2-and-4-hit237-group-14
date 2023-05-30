from .models import *
from django import forms
from django.forms import ModelForm


class FormOrganization(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Organization
        fields = '__all__'

class FormRole(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Role
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

class FormAudit(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Audit
        fields = '__all__'
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'class': 'datetimepicker'}),
        }