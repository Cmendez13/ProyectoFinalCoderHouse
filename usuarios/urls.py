from django.urls import path
from usuarios.views import *
from django.contrib.auth import views




urlpatterns = [
    
    path('login/',login_request,name='login'),
    path('signup/',register_request,name='registro'),
    path('logout',LogoutView.as_view(template_name='logout'),name='logout'),
    path('creaperfil/',PerfilUsuarioView.as_view(),name='crea-perfil'),
    path('perfil/',PerfilUsuarioView.as_view(),name='perfil'),
]
