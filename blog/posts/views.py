from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Post

# Create your views here.
class PostListView(ListView):

    model = Post
    template = "post_list.html"


class PostDetailView(DetailView):
	model = Post
	template_name = 'posts/post_detail.html'