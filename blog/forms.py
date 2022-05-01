from django import forms
from blog.models import *
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    
    class Meta:
        model=Post
        fields=('titulo','autor','contenido','etiqueta')

        widgets={
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'autor':forms.TextInput(attrs={'class':'form-control','value':'','id':'autor','type':'hidden'}),
            'contenido':forms.Textarea(attrs={'class':'form-control'}),
            'etiqueta':forms.TextInput(attrs={'class':'form-control'}),
          }


class ComentForm(forms.ModelForm):
    
    class Meta:
        model=Comentario
        fields=('autor','contenido')

        widgets={
            'autor':forms.TextInput(attrs={'class':'form-control','value':'','id':'autor','type':'hidden'}),
            'contenido':forms.Textarea(attrs={'class':'form-control'}),
        }


class ContactForm(forms.ModelForm):

    class Meta:
        model=Clientes
        fields=('__all__')

        widgets={
              'nombre':forms.TextInput(attrs={'class':'form-control','value':'','id':'autor','type':'hidden'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'mensaje':forms.TextInput(attrs={'class':'form-control'}),
         }
