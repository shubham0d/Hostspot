import datetime
from django import forms
from .models import DefaultConf
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class SetupForm(forms.ModelForm):
    class Meta:
        model = DefaultConf
        fields = ('url','expireDate', 'hostingType')

class UploadFileForm(forms.Form):
    file = forms.FileField()

class HostingForm(forms.Form):
    #renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    #body = forms.CharField(widget = forms.Textarea)
    hostingType = forms.ChoiceField(label = "Hosting type",help_text='type of content you want to host', choices = [('W', 'Website'), ('V', 'Video'), ('I', 'Image'), ('O', 'Other')])
    expireDays = forms.DecimalField(label = "Expire Days", initial=14, max_value = 14, min_value = 1)
    domain = forms.CharField(label = "Domain name(Optional)", required = False, help_text='Domain to host on. Should be in form xyz.abc')
