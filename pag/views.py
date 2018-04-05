from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.filter(fecha_publicado__lte=timezone.now()).order_by('fecha_publicado')
	return render(request, 'pag/post_list.html', {'posts':posts})

def post_detalles(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'pag/post_detalles.html', {'post': post})

# Create your views here.
