from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import  Post
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView , CreateView , UpdateView

posts = [
    {
        'author' : 'CoreyMS',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'August 27, 2018'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'August 28, 2018'
    }
]

# def home(request):
#     return HttpResponse('<h1>Blog Home</h1>')
def home(request):
    context = {
        # 'post' : posts
        'post': Post.objects.all()
    }
    return render (request, 'blog/home.html' , context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'post'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



# def about(request):
#     return HttpResponse('<h1>Blog About</h1>')
def about(request):
    return render (request, 'blog/about.html' , {'title' : '!!!TEST'} )

