from django import forms
from django.forms import ModelForm

from .models import OwnerBranch

class OwnerForm(ModelForm):
    class Meta:
        model = OwnerBranch
        fields = ('branch','user',)
