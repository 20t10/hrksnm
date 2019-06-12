from django import forms
from django.forms import ModelForm

from .models import Branch,  BranchWithdraw


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('branch_name','branch_img','branch_address','branch_district','branch_amphoe','branch_province','branch_zipcode','branch_postcode','tel_number',)

class BranchUpdateForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('branch_name','branch_img','branch_address','branch_district','branch_amphoe','branch_province','branch_zipcode','branch_postcode','branch_postcode','tel_number','tel_number_two','tel_number_three',)




# class MonthlyMoneyForm(forms.ModelForm):
#     class  Meta:
#         model = MonthlyMoney
#         fields = ('user_save','branch','check_money')
# class MonthlyMoneyUpdateForm(forms.ModelForm):
#     class  Meta:
#         model = MonthlyMoney
#         fields = ('check_money',)

class CreateWithdraw(forms.Form):
    user = forms.CharField(label='ผู้บันทึก',
                               widget=forms.TextInput(attrs={"class": "form-control", }))
    branch = forms.CharField(label='สาขา',
                                  widget=forms.TextInput(attrs={"class":"form-control",}))
    money = forms.CharField(label='จำนวนเงิน',
                                  widget=forms.NumberInput(attrs={"class":"form-control",}))

class BranchWithdrawForm(forms.ModelForm):
    class  Meta:
        model = BranchWithdraw
        fields = ('branch','branch_check_money')

class BranchWithdrawUpdateForm(forms.ModelForm):
    class  Meta:
        model = BranchWithdraw
        fields = ('branch_check_money',)
