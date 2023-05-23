from django import forms
from myApplication.models import Memory

class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['place_name', 'comment']
