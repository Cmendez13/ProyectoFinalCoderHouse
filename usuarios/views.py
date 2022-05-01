from . import views
from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.models import User
from blog.views import homeview
from usuarios.forms import *
from django.contrib import messages
#Autenticación Django
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

# Create your views here.
class RegistroUsuarioView(generic.CreateView):
    form_class=UserRegisterForm
    template_name='registration/registro.html'

    def get_success_url(self):

        return homeview
    
class PerfilUsuarioView(generic.CreateView):

    form_class=PerfilUsuarioForm
    template_name='registration/RegPerfil.html'

    def get_success_url(self):
        return reverse('perfil')


def login_request(request): 

    if request.method == 'POST':   
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not  None:
                login(request, user)
                usuario = form.cleaned_data['username']
                return render(request, "blog/post-list.html", {'msj':f'Bienvenido {usuario}!'})
            
            else:
                return render(request, 'login.html', {'form':form},)

        else:
            return render(request, 'usuarios/login.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'usuarios/login.html', {'form':form})
         


def register_request(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/registro.html', {'form': form})