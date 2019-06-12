from django import forms
from django.forms import ModelForm
from .models import managesite, serviceimg, faqsite

class SiteForm(forms.ModelForm):

    class Meta:
        model = managesite
        fields = ('icon','brand','welcome','about','service','contact',)

class SlideForm(forms.ModelForm):
    class Meta:
        model = serviceimg
        fields =('img','detail',)

class FAQForm(forms.ModelForm):
    class Meta:
        model = faqsite
        fields = ('question','answered',)