from django import forms
from .models import Input, FileInput


class InputModelForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = ['article']

class FileInputModelForm(forms.ModelForm):
    class Meta:
        model = FileInput
        fields = ['articles']


