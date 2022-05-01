from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    avatar=models.ImageField(null=True,blank=True,upload_to="images",default="static/images/avatar_predeterminado.png")
    biografia=models.TextField()
    web=models.CharField(max_length=255,null=True,blank=True)
    instagram=models.CharField(max_length=255,null=True,blank=True)
    facebook=models.CharField(max_length=255,null=True,blank=True)
    twitter=models.CharField(max_length=255,null=True,blank=True)
    linkedin=models.CharField(max_length=255,null=True,blank=True)
    youtube=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self): 
        return str(self.usuario)


