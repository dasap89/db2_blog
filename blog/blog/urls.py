from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from accounts.views import LoginView, SignupView
from posts.views import PostListView, PostDetailView, PostLikeAPIToggle
from comments.views import add_comment_to_post
from django.conf.urls.static import static

from django.contrib import admin


urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="index.html"), name="home"),
    url(r'^account/signup/$', SignupView.as_view(), name="account_signup"),
    url(r'^account/login/$', LoginView.as_view(), name="account_login"),
    url(r'^account/', include("account.urls")),
    url(r'^posts/$', login_required(PostListView.as_view(), login_url='/account/login/'), name="post_list"),
    url(r'^posts/(?P<pk>\w+)/$', login_required(PostDetailView.as_view(), login_url='/account/login/'), name="post_detail"),
    url(r'^posts/(?P<pk>\w+)/like/$', login_required(PostLikeAPIToggle.as_view(), login_url='/account/login/'), name="post_like"),
    url(r'^post/(?P<pk>\d+)/comment/$', add_comment_to_post, name='add_comment_to_post'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
