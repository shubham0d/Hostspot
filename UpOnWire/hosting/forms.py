from django import forms
from .models import DefaultConf

class SetupForm(forms.ModelForm):
    class Meta:
        model = DefaultConf
        fields = ('url','expireDate', 'hostingType')

class UploadFileForm(forms.Form):
    file = forms.FileField()
