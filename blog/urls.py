from django.conf.urls import url
from .views.details import SlugDetailView,CategoryDetailView
from .views.listings import PostList,AddSearch,SearchList
from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$',PostList.as_view(),name='home'),
        url(r'^(?P<slug>[-\w]+)$',SlugDetailView.as_view(),name='postslugdetail'),
        url(r'^category/(?P<slug>[-\w]+)$',CategoryDetailView.as_view(),name='categorydetail'),
        url(r'^addsearch$',AddSearch.as_view(),name='startseacrh'),
        url(r'^search/(?P<keyword>[-\w]+)$',SearchList.as_view(),name='search'),
    ]
