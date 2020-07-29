from django import forms
from dict.models import Word


class CreateWordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['name', 'translate', 'transcription', 'phrase', 'sentence']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'translate': forms.TextInput(attrs={'class': 'form-control'}),
            'transcription': forms.TextInput(attrs={'class': 'form-control'}),
            'phrase': forms.TextInput(attrs={'class': 'form-control'}),
            'sentence': forms.TextInput(attrs={'class': 'form-control'}),
        }
