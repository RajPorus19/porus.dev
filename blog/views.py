from django.shortcuts import render
from .models import Post
from django.db.models import Q
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# Create your views here.
def blog(request):
    try :
        q = request.GET.get('q')
    except :
        q = None
    if(q):
        context = {
            'posts' : Post.objects.filter(Q(title__icontains=q) | Q(content__icontains=q)),
            #'posts' : Post.objects.annotate(search=SearchVector('title', 'content')).filter(search=q),
            'noPost' : False,
            'arg' : q,
        }
    else:
        context = {
            'posts' : Post.objects.all(),
            'noPost' : False,
            'arg' : q,
        }
    if(len(context['posts'])==0):
        context = {
            'noPost' : True,
            'arg' : q,
        }
    
    return render(request, 'blog/blog.html', context)

class PostDetailView(DetailView):
    model = Post

