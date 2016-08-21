"""HackerNews URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from crawler.views import (NewsItemListView, home, user_logout, user_login, sign_up, delete_news, read_news)

from algo_app.views import algo_view

from AlbumApi.views import AlbumPhotoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'albumphoto', AlbumPhotoViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^news/$', login_required(NewsItemListView.as_view()), name='news_list'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^sign_up/$', sign_up, name='sign_up'),
    url(r'^login/$', user_login, name='login'),
    url(r'^algo/$', algo_view, name='algo'),
    url(r'^news/delete/(?P<pk>\d+)/$', login_required(delete_news), name='delete_news'),
    url(r'^news/read/(?P<pk>\d+)/$', login_required(read_news), name='read_news'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
