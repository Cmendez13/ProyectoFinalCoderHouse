from re import L
from django import views
from django.urls import path
from blog.views import *
from . import views



urlpatterns = [
    
    path('',homeview.as_view(),name='home'),
    path('nosotros/',acerca_de_nosotros,name='acerca-de'),
    path('post/<int:pk>',ListarPosts.as_view(),name='post-detail'),
    path('creaPost/',CrearPosts.as_view(),name='crea-post'),
    path('post/mod/<int:pk>/',EditPost.as_view(),name='edit-post'),
    path('post/<int:pk>/borrar',BorrarPost.as_view(),name='delete-post'),
    path('post/<int:pk>/comentaPost/',CrearComentario.as_view(),name='comenta-post'),
    path('search/',views.consulta_Post,name="post_search"),
    path('contacto/',Contacto.as_view(),name="contato"),
    path('like/<int:pk>',LikeView,name='like-post'),
]
