from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.views import HomeView
urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^accounts/todo/',include('todo.urls',namespace='todo')),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^calender/',include('calender.urls',namespace='calender')),
    url(r'^admin/', include(admin.site.urls)),
)
