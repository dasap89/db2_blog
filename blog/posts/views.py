from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import Post


class PostListView(ListView):
    model = Post
    template = "post_list.html"
    paginate_by = 3


class PostDetailView(DetailView):
	model = Post
	template_name = 'posts/post_detail.html'


class PostLikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk=None):
        
        post_obj = get_object_or_404(Post, pk=pk)
        url_ = post_obj.get_absolute_url()
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated():
            if user in post_obj.like.all():
                liked = False
                post_obj.like.remove(user)
            else:
                liked = True
                post_obj.like.add(user)
            updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)