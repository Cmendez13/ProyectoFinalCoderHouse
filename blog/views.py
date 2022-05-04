from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from blog.models import *
from blog.forms import *
from django.db.models import Count
from django.urls import reverse
from django.http import HttpResponseRedirect

#Autenticación Django

from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



def inicio(request):
 
    return render(request,'blog/inicio.html')

class homeview(ListView):
    model=Post
    template_name='blog/post-list.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ListarPosts(DetailView):
    model=Post
    template_name='blog/posts.html'
    #paginated_by=4

    def get_context_data(self,*args, **kwargs):
        contexto= super(ListarPosts, self).get_context_data(*args, **kwargs)
        objeto_like = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = objeto_like.total_likes()
        contexto['total_likes']= total_likes
        return contexto


class CrearPosts(LoginRequiredMixin,CreateView):
    model=Post
    form_class=PostForm
    template_name='blog/crea-post.html'

class EditPost(LoginRequiredMixin,UpdateView):

    model = Post
    form_class= PostForm
    template_name="blog/editPost.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto.update({
            'tipo_template': 'Editar' 
        })
        return contexto

class BorrarPost(LoginRequiredMixin,DeleteView):
    model=Post
    template_name="blog/borraPost.html"
    
    def get_success_url(self):
        return reverse('home')

class CrearComentario(LoginRequiredMixin,CreateView):
    model=Comentario
    form_class=ComentForm
    template_name='blog/comentario.html'
    success_url = "/"

    def form_valid(self,form):        
        form.instance.post_id = self.kwargs['pk']
        form.instance.autor = self.request.user
        return super().form_valid(form)


 

def consulta_Post(request):
    query=request.GET['query']
    allPosts= Post.objects.filter(titulo__icontains=query)
    total=allPosts.count()
    params={'allPosts': allPosts,'total':total}

    return render(request, 'blog/busqueda.html', params)

class ResultadosConsultaView(ListView):
    model=Post
    template_name="blog/busqueda.html"

    def get_queryset(self):
        consulta=self.request.GET.get("q")
        resultados=Post.objects.filter(contenido__icontains='mi')

        return resultados

def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail',args=[pk]))
    
class Contacto(CreateView):
    model=Clientes
    form_class=ContactForm
    template_name='blog/contacto.html'

def acerca_de_nosotros(request):
    return render(request,'blog/acerca-de-nosotros.html')
