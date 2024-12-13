from django import forms
from django.template.defaultfilters import title

from .models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'type': 'password', 'required': 'required'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'type': 'password', 'required': 'required'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'type': 'text', 'required': 'required'}))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username','password', 'confirm_password')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input','type':'text','required': 'required'}),
            'last_name': forms.TextInput(attrs={'class': 'input','type':'text' ,'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'input','type':'email','required': 'required'}),
        }

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        raise forms.ValidationError("Passwords don't match")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username


class LoginForm(forms.Form):
    username = forms.CharField(max_length=300, widget=forms.TextInput(
        attrs={
            'class': 'input_field',
            'type':'text',
            'required': 'required',
            'id':'email_field',
            'name': 'input-name',
            'title': 'inpit title',
            'placeholder': 'Enter Your Username or Email',
               }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input_field',
            'type': 'password',
            'required': 'required',
            'id': 'password_field',
            'name': 'input-name',
            'title': 'inpit title',
            'placeholder': 'Password',
        }
    ))