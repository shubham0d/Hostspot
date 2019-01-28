from django import forms
from .models import DefaultConf

class SetupForm(forms.ModelForm):
    class Meta:
        model = DefaultConf
        fields = ('imageId','url','expireDate', 'hostingType')

class UploadFileForm(forms.Form):
    file = forms.FileField()
