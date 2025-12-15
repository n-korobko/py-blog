from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
