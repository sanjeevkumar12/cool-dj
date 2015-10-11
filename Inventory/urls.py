from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from blog.views.details import SlugDetailView
from blog.views.listings import PostList
from blog.views.details import CategoryDetailView,TagDetailView,AuthorView
from blog.views import archive as ArchiveViews
urlpatterns = patterns('',
    url(r'^$', PostList.as_view(), name='home'),
    url(r'^accounts/todo/',include('todo.urls',namespace='todo')),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^calender/',include('calender.urls',namespace='calender')),
    url(r'^blog/',include('blog.urls',namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^category/(?P<slug>[-\w]+)',CategoryDetailView.as_view(),name='categorydetail'),
    url(r'^tags/(?P<slug>[-\w]+)',TagDetailView.as_view(),name='tagdetail'),
    url(r'^author/(?P<slug>[-\w]+)',AuthorView.as_view(),name='authordetail'),
    url(r'^(?P<slug>[-\w]+)$',SlugDetailView.as_view(),name='postslugdetail'),
    url(r'^(?P<year>\d{4})/(?P<month>\w+)/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',SlugDetailView.as_view(), name='archive_post_detail'),
    url(r'^(?P<year>\d{4})/$',ArchiveViews.YearlyView.as_view(), name='post_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w+)/$',ArchiveViews.MonthlyView.as_view(), name='post_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$',ArchiveViews.DateView.as_view(), name='post_archive_day'),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)