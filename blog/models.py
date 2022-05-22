from django.db import models
from datetime import datetime
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    titulo=models.CharField(max_length=200)
    autor=models.ForeignKey(User,on_delete=models.CASCADE)
    contenido=RichTextField(blank=True,null=True)
    etiqueta=models.CharField(max_length=200,default='math')
    fecha_creacion=models.DateField(auto_now=datetime.now())
    likes=models.ManyToManyField(User,related_name='blog_post')


    def __str__(self):
        return self.titulo + ' ('+self.autor+')'

    class Meta:
        ordering=['-pk']

    
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    def total_likes(self):
    
        return self.likes.count()

    @property
    def get_comentarios_count(self):
        return self.comentarios.all().count()

class Comentario(models.Model):
    autor = models.CharField(max_length=255)
    post = models.ForeignKey(Post, related_name="comentarios", on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField('contenido', null=False, blank=False)

    def __str__(self):
        
        return f'{self.autor}'

class Clientes(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    email=models.EmailField()
    mensaje=models.CharField(max_length=255)
