from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from blog.views.details import SlugDetailView
from blog.views.listings import PostList
from blog.views.details import CategoryDetailView,TagDetailView
urlpatterns = patterns('',
    url(r'^$', PostList.as_view(), name='home'),
    url(r'^accounts/todo/',include('todo.urls',namespace='todo')),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^calender/',include('calender.urls',namespace='calender')),
    url(r'^blog/',include('blog.urls',namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^category/(?P<slug>[-\w]+)',CategoryDetailView.as_view(),name='categorydetail'),
    url(r'^tags/(?P<slug>[-\w]+)',TagDetailView.as_view(),name='tagdetail'),
    url(r'^(?P<slug>[-\w]+)$',SlugDetailView.as_view(),name='postslugdetail'),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
