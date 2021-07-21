from django.forms import ModelForm, Textarea
from .models import task_info
from django import forms

class task_infoForm(ModelForm):
    
    class Meta:
        model = task_info
        fields = '__all__'
        widgets = {
            'title': Textarea(attrs={'class':'input'}),
            'details': Textarea(attrs={'class':'details_input'})
        }
