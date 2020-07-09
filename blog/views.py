from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.paginator import Paginator
from django.views import generic
from .models import Post, PostContent

class PostListView(generic.ListView):
    model = Post
    template_name = "blog/PostListView.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    
    paginate_by = 2


class PostPage(generic.DetailView):

    model = Post

    template_name = "blog/PostPage.html"
    context_object_name = "post"
