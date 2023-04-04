from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from core.models import Post


class IndexBlogView(TemplateView):
    template_name = "index.html"


class ListarPostsListView(ListView):
    context_object_name = 'posts'
    template_name = 'blog/post/listarposts.html'
    queryset = Post.publicados.all()

