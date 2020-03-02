from django.shortcuts import render
from django.http import HttpResponseRedirect #para hacer el redireccionamiento a otra pag

# Create your views here.
from .models import Post
from .forms import PostForm

#Funcion para mostrar la lista de post
def post_list(request):
    posts=  Post.objects.all()
    context = {
        'post_list': posts 
    } 
    return render(request, "post_list.html",context)

#Funcion para mostrar el id de un post en especifico
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, "post_detail.html", context)

#Para crear un formulario
def post_create(request):
    #este es para hacer el POST request http, solo si es POST
    form = PostForm(request.POST or None) 
    #si tiene contenido y titulo entonces salvara el form
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/post') #con el #permite retornar a otra pag
        #Con el context se esta trabajando tambien con 
        #el GET request http
    context = {
         "form": form,
         "form_type" : 'Create' 
    }
    return render(request, "post_create.html", context)

def post_update(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post) 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/post') 
    context = {
     "form": form,
     "form_type" : 'Update' 
    }   
    return render(request, "post_create.html", context)

def post_detele(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/post')