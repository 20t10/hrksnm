from django import forms
from django.forms import ModelForm
from branches.models import Branch
from machines.models import BranchMachine
from .models import TodoList, Notification, MachineMaintained

class  Maintained(forms.ModelForm):
    class Meta:
        model = MachineMaintained
        fields=('branch','tech_name','work',)

class  TechMaintained(forms.ModelForm):
    class Meta:
        model = MachineMaintained
        fields=('comment','price',)
class  MaintainedConfirm(forms.ModelForm):
    class Meta:
        model = MachineMaintained
        fields=('branch','tech_name','status',)
#emp actions
class TodoCreateForm(forms.ModelForm): #emp admin > to tech
    class Meta:
        model = TodoList
        fields = ('work_fix','work_location','work_machine','tech_name',)

class ConfirmTodo(forms.ModelForm):# admin emp do this admin

    class Meta:
        model = TodoList
        fields = ('confirm_photo','work_status',)

#tech action

class TechSend(forms.ModelForm): #tech confirm fix
    class Meta:
        model = TodoList
        fields = ('confirm_photo','price', 'comment',)

class CreateNotiForm(forms.ModelForm):# any1 send
    class Meta:
        model = Notification
        fields = ('user_send','user_receive','branch','machine', 'fix_description_extra',)

class SendNotiForm(forms.ModelForm):# any1 send
    class Meta:
        model = Notification
        fields = ('user_send','branch','machine', 'fix_description_extra',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['machine'].queryset = BranchMachine.objects.none()
        if 'branch' in self.data:
            try:
                branch_id = int(self.data.get('branch'))
                #print(branch_id)
                self.fields['machine'].queryset = BranchMachine.objects.filter(machine_location_id=branch_id).order_by('machine_name')
                print(BranchMachine.objects.filter(machine_location_id=branch_id).order_by('machine_name'))

            except (ValueError, TypeError):
                print(ValueError, TypeError)
                # pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['machine'].queryset = self.instance.branch.machine_id_set.order_by('machine_name')

class BrokenUpdateForm(forms.ModelForm): #update what? action tech
    class Meta:
        model = Notification
        fields = ('work_status',)

class FixUpdateForm(forms.ModelForm): #not sure action tech
    # id = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly','label':'IDการซ่อม'}))
    # branch = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control ",'readonly':'readonly'}))
    # machine = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'readonly':'readonly'}))
    # fix_description_extra = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control ",'readonly':'readonly'}))

    class Meta:
        model = Notification
        fields = ('work_status',)
