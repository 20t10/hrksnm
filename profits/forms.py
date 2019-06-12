from django import forms
from django.forms import ModelForm
from .models import ProfitMachine

class CreateProfit(forms.ModelForm):
    class Meta:

        model = ProfitMachine
        fields = ('branch','machine','check_money','fix_money')

class UpdateProfit(forms.ModelForm):

    class Meta:
        model = ProfitMachine
        fields = ('branch','machine','check_money','fix_money')