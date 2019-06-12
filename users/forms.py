from django import forms
from django.forms import ModelForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout, get_user_model
User = get_user_model()


class CreateUser(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','first_name','last_name','organization','email','user_type',)
    def __init__(self, *args, **kwargs):
        super(CreateUser, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'รหัสผ่านขั้นต่ำ8ตัวอักษร เป็นตัวอักษรภาษาอังกฤษ ผสมกับตัวเลขได้'
        self.fields['password2'].help_text = 'กรอกรหัสผ่านอีกครัง'

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control ","placeholder":"password"}))

    def clean(self, *args,**kwargs):
        username =self.cleaned_data.get("username")
        password =self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("username หรือ password ไม่ถูกต้อง กรุณาเช็คใหม่อีกครั้ง!")
            if not user.check_password(password):
                raise forms.ValidationError("รหัสผ่านไม่ถูกต้อง")
        return super(LoginForm, self).clean(*args,**kwargs)


ROLE_CHOICES = (
    ('Admin','Admin'),
    ('Employee','Employee'),
    ('Owner','Owner'),
    ('Technician','Technician'),
)

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={"class":"form-control","placeholder":"ชื่อผู้ใช้งาน"}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"รหัสผ่าน"}))
    confirmpassword = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"ยืนยันรหัสผ่าน"}))
    email = forms.EmailField(label='E-Mail',widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"E-mail"}))
    first_name = forms.CharField(label='First Name',widget=forms.TextInput(attrs={"class":"form-control","placeholder":"ชื่อ"}))
    last_name =forms.CharField(label='Last Name', widget=forms.TextInput(attrs={"class":"form-control","placeholder":"นามสกุล"}))
    role_user = forms.CharField(label='Role',widget=forms.Select(choices=ROLE_CHOICES))
    def clean_username(self):
        username = self.cleaned_data.get('username')
        ### check Username###############
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("เกิดข้อผิดพลาด username นี้ไม่สามารถใช้งานได้")

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        ### check Username###############
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("เกิดข้อผิดพลาด email ถูกใช้แล้ว")
        return email

    def clean_confirmpassword(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        confirmpassword = self.cleaned_data.get('confirmpassword')
        ### เช็ค ยืนยันพาสเวิด
        if password != confirmpassword:
            raise forms.ValidationError("รหัสผ่าน ไม่ตรงกัน")
        if len(password) < 8:
            raise forms.ValidationError("รหัสผ่านควรมีตั้งแต่ 8ตัวขึ้นไป")
        return data

class UpdateUserForm(forms.ModelForm):
    email=  forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"})),
    first_name =  forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"})),
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"})),
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','organization',]
