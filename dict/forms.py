from django import forms
from dict.models import Word


class CreateWordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = '__all__'
