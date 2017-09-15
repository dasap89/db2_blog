"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from accounts.views import LoginView, SignupView
from posts.views import PostListView, PostDetailView

from django.contrib import admin


urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="index.html"), name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^account/signup/$', SignupView.as_view(), name="account_signup"),
    url(r'^account/login/$', LoginView.as_view(), name="account_login"),
    url(r'^account/', include("account.urls")),
    url(r'^posts/$', PostListView.as_view(), name="post_list"),
    url(r'^posts/(?P<pk>\w+)/$$', PostDetailView.as_view(), name="post_list"),
]
