from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    last_name = forms.CharField(
        label='Họ và tên',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    birth_date = forms.DateField(
        label='Ngày / Tháng / Năm Sinh',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        label='Số điện thoại',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Mật khẩu',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Nhập lại mật khẩu',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model=User
        fields = ['last_name','email','birth_date','email','phone_number','password1','password2']