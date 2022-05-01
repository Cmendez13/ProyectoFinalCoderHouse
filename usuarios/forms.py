from django import forms
from blog.models import *
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from usuarios.models import *

class UserRegisterForm(UserCreationForm):
    username=forms.CharField(max_length=255)
    email=forms.EmailField()
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repita la Contraseña',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_text={k:"" for k in fields}

class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField()


class PerfilUsuarioForm(ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        widgets={
            'usuario':forms.TextInput(attrs={'class':'form-control','value':'','id':'autor','type':'hidden'}),
            'avatar':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'biografia':forms.Textarea(attrs={'class':'form-control'}),
            'web':forms.TextInput(attrs={'class':'form-control'}),
            'instagram':forms.TextInput(attrs={'class':'form-control'}),
            'facebook':forms.TextInput(attrs={'class':'form-control'}),
            'twitter':forms.TextInput(attrs={'class':'form-control'}),
            'linkedin':forms.TextInput(attrs={'class':'form-control'}),
            'linkedin':forms.TextInput(attrs={'class':'form-control'}),
             }     
          