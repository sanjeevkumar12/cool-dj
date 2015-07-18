from django.conf.urls import url
from .views.details import SlugDetailView,CategoryDetailView
from .views.listings import PostList
from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$',PostList.as_view(),name='home'),
        url(r'^(?P<slug>[-\w]+)$',SlugDetailView.as_view(),name='postslugdetail'),
        url(r'^category/(?P<slug>[-\w]+)$',CategoryDetailView.as_view(),name='categorydetail'),

    ]
