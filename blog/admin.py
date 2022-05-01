from django.contrib import admin

from usuarios.models import Perfil

from .models import Comentario, Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('titulo','autor','fecha_creacion')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display=('autor','post','fecha_publicacion')


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display=('usuario','avatar')

