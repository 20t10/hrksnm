from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms
from django.forms import ModelForm
from .models import BranchMachine,MachineLog,MachineReal


class MachineLogCreate(forms.ModelForm):
    class Meta:
        model = MachineLog
        fields =(
            'log_module',
            'log_branch',
            'log_thb',

        )

class MachineLogUpdate(forms.ModelForm):
    class Meta:
        model = MachineLog
        fields =(

            'log_module',
            'log_branch',

        )

class MachineRealCreate(forms.ModelForm):
    class Meta:
        model = MachineReal
        fields =(
            'real_id',
            'machine',

        )

class MachineRealUpdate(forms.ModelForm):
    class Meta:
        model = MachineReal
        fields =(

            'real_id',
            'machine',

        )


class MachineRealCreate(forms.ModelForm):
    class Meta:
        fields = ('machine',)

class MachineFormCreate(forms.ModelForm):
    class Meta:
        model = BranchMachine
        fields = ('machine_name',)

class MachineFormUpdate(ModelForm):
    class Meta:
        model = BranchMachine
        fields = ('machine_location','machine_name','next_fix',)
